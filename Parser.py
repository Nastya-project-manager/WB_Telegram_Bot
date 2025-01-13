import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
from log_config import *

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'}


# Получение категорий меню
def get_server_menu():
    """
    Функция получение json категорий. Отправляем запрос на сервер static-basket-01.wbbasket.ru
    :return: Any
    """
    url_menu = 'https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v3.json'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'}

    response = requests.get(url_menu, headers)

    if response.status_code == 200:
        # Пришел все меню, Возьму только для женщин
        data = response.json()[4]["childs"]
        df = pd.DataFrame(data)
        df = df[~df['childs'].apply(lambda x: isinstance(x, list))]
        df.to_csv("wildberries_menu.csv", index=True)
    else:
        logging.error(f'Ошибка запроса: {response.status_code}')


# Получение товаров в категории
def get_products(name, shard, query):
    """
    Функция, которая будет получать первые 100 продуктов в данной категории
    (Берем только 100 так как есть ограничения у сервера когда он получает слишком много запросов с одного IP-адреса в
     течение определённого периода времени)

    :param name: Название категории
    :param shard: Путь категории на сайте
    :param query: Параметр запроса из меню
    :return:
    """
    data = {
        'name': name,
        'shard': shard,
        'query': query,
        'products': []
    }
    url_products = f'https://catalog.wb.ru/catalog/{shard}/v2/catalog?ab_testing=false&appType=1&{query}&curr=rub&dest=-2689194&hide_dtype=10&lang=ru&page=1&sort=popular&spp=30&uclusters=2&uiv=8'
    response = requests.get(url_products, headers)
    """если нужно взять все товары"""
    # js = response.json()
    # total = (js['data']['total'] + 100 - 1) // 100 Узнаем сколько всего станиц
    # for i in range(1, total + 1):
    #     url_products = f'https://catalog.wb.ru/catalog/{shard}/v2/catalog?ab_testing=false&appType=1&{query}&curr=rub&dest=-2689194&hide_dtype=10&lang=ru&page={i}&sort=popular&spp=30&uclusters=2&uiv=8'
    #     response = requests.get(url_products, headers)
    #     if response.status_code == 200:
    #         js = response.json()
    #         for item in js['data']['products']:
    #             product = {
    #                 'id': item['id'],
    #                 'name': item['name'],
    #                 'colors': ', '.join(a['name'] for a in item['colors']),
    #                 'brand': item['brand'],
    #                 'rating': item['reviewRating'],
    #                 'feedbacks': item['feedbacks'],
    #                 'price': [{a['name']: a['price']['total'] // 100} for a in item['sizes']],
    #                 'url': f'https://www.wildberries.ru/catalog/{item['id']}/detail.aspx'
    #             }
    #             data['products'].append(product)
    #     else:
    #         print(response.status_code)
    #         print(url_products)
    #         break
    """Берем первые 100"""
    if response.status_code == 200:
        js = response.json()
        for item in js['data']['products']:
            product = {
                'id': item['id'],
                'name': item['name'],
                'colors': ', '.join(a['name'] for a in item['colors']),
                'brand': item['brand'],
                'rating': item['reviewRating'],
                'feedbacks': item['feedbacks'],
                'price': [{a['name']: a['price']['total'] // 100} for a in item['sizes']],
                'url': f'https://www.wildberries.ru/catalog/{item['id']}/detail.aspx'
            }

            data['products'].append(product)
    return data


def analysis(products):
    """
    Функция анализирует среднюю стоимость товара
    и считает метрику по соотношению цены и отзывов
    :return: Any
    """
    # Создание DataFrame
    df = pd.DataFrame(products)

    # Вычисление средней цены
    df['average_price'] = df['price'].apply(lambda x: sum(list(d.values())[0] for d in x) / len(x))

    # Вычисление метрики
    df['quality_metric'] = (df['rating'] * df['feedbacks']) / df['average_price']

    # Найти строку с максимальной метрикой качества
    best_product = df.loc[df['quality_metric'].idxmax()]

    return best_product


# Функция для проверки доступности ссылки
def check_url(num, id):
    url = f"https://basket-{num:02d}.wbbasket.ru/vol{id[:len(id) - 5]}/part{id[:len(id) - 3]}/{id}/images/c516x688/1.webp"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return url  # Возвращаем ссылку, если код 200
    except requests.exceptions.RequestException:
        pass  # Если ошибка, просто пропускаем


# Главная функция для параллельной проверки
def check_urls_parallel(id: str):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_url, num, id): num for num in range(1, 26)}

        # Проверяем по мере завершения запросов
        for future in as_completed(futures):
            url = future.result()
            if url:  # Если ссылка вернула 200
                executor.shutdown(wait=False)  # Завершаем все потоки сразу
                return url  # Останавливаем выполнение после нахождения первого успешного запроса
        else:
            print("Все ссылки недоступны или ошибка сети.")


