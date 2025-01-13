import requests
import pandas as pd


# Получение категорий меню
def get_server_menu():
    """
    Получение json из static-basket-01
    :return: json
    """
    url_menu = 'https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v3.json'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'}

    response = requests.get(url_menu, headers)

    if response.status_code == 200:
        # Пришел все меню, Возьму только для женщин
        data = response.json()[4]["childs"]
        return data
    else:
        print(f'Ошибка запроса: {response.status_code}')


def get_products(name, shard, query):
    """
    Получение товаров в данной категории
    :param name:
    :param shard:
    :param query:
    :return: dict
    """
    data = {
        'name': name,
        'shard': shard,
        'query': query,
        'products': []
    }
    url_products = f'https://catalog.wb.ru/catalog/{shard}/v2/catalog?ab_testing=false&appType=1&{query}&curr=rub&dest=-2689194&hide_dtype=10&lang=ru&page=1&sort=popular&spp=30&uclusters=2&uiv=8'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'}
    response = requests.get(url_products, headers)
    js = response.json()
    total = (js['data']['total'] + 100 - 1) // 100
    for i in range(1, total + 1):
        url_products = f'https://catalog.wb.ru/catalog/{shard}/v2/catalog?ab_testing=false&appType=1&{query}&curr=rub&dest=-2689194&hide_dtype=10&lang=ru&page={i}&sort=popular&spp=30&uclusters=2&uiv=8'
        response = requests.get(url_products, headers)
        js = response.json()
        for item in js['data']['products']:
            product = {
                'id': item['id'],
                'name': item['name'],
                'brand': item['brand'],
                'rating': item['reviewRating'],
                'price': [{a['name']: a['price']['total'] // 100} for a in item['sizes']]
            }
    return data
    # reviewRating рейтинг

    #https://basket-14.wbbasket.ru/vol2302/part230236/230236844/info/ru/card.json - Инфа по карте
    #https://basket-14.wbbasket.ru/vol2302/part230236/230236844/info/price-history.json - Истории


# print(get_server_menu())
# get_products('Блузки и рубашки', 'bl_shirts', 'cat=8126')
