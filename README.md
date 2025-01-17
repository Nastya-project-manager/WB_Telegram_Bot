# WB_Telegram_Bot
Telegram bot для анализа товаров в WB
Делимся с вами ссылкой для использования бота : https://t.me/training_script_bot
Наш проект представляет собой Telegram-бот, предназначенный для поиска лучших предложений на платформе Wildberries. Бот анализирует товары в различных категориях, которые мы ему прописали в файле wildberries_menu.csv на основе данных с сайта, определяет их качество и стоимость на основе отзывов, рейтингов и средней цены, а также предоставляет пользователям ссылки и изображения товаров.
# Основные функции:
1. Категории товаров: Возможность выбрать категорию товара из предостановленного списка, который появляется, когда пользователь нажимает start.
2. Анализ качества товара: Расчет метрики качества на основе рейтинга, количества отзывов и средней цены.
![Иллюстрация к проекту](photo/photo_2025-01-10_23-48-18.jpg)
4. Предоставление информации о товарах: Название, цвет, бренд, рейтинг, отзывы, средняя цена, метрика качества и изображение.
5. Уведомления об ошибках: Логирование критических ошибок с уведомлением администратора.
6. Интуитивно понятный интерфейс: Бот имеет удобную навигацию через inline-кнопки.
# Описание модулей:
1. init.py: этот файл импортирует все обработчики из директории handlers и keyboard и позволяет их зарегистрировать через main.py.
2. bot_commands.py: обрабатывает команду /start, приветствует пользователя и показывает кнопки с категориями товаров.
3. bot_errors.py: ловит ошибки, отправляет сообщение админу о них и логирует критические ошибки.
4. bot_messages.py: обрабатывает сообщения, которые не попадают под другие обработчики, повторяет сообщение пользователя и если сообщение невозможно обработать, отправляет текст: "Понял, спасибо!".
5. bot_startup.py: логирует запуск бота и загружает актуальное меню с Wildberries.
6. callback_query.py: обрабатывает нажатия на inline-кнопки, получает товары из выбранной категории, анализирует их и отправляет информацию пользователю.
7. categories_key.py: создает inline-кнопки для категорий товаров.
8. Parser.py: работа с API Wildberries (загружает список категорий, получает товары и анализирует их).
9. main.py: регистрирует обработчики и запускает бота.
10. log_config.py: записывает логи в консоль и файл bot.log.
11. wildberries_menu.csv: хранит список категорий, загруженный с Wildberries.
12. .env: хранит токен бота.
# Инструкция по запуску кода:
1. Установка окружения
Перед запуском проекта необходимо подготовить рабочую среду. Следуйте шагам ниже.

Шаг 1: Скачивание проекта
Скачайте проект с репозитория GitHub.

![image_2025-01-14_12-52-25](https://github.com/user-attachments/assets/8e8a26ba-88c3-4c9e-ba54-888b300d4667)

Зайдите в проект в github и нажмите на кнопку Code, как указано на фотографии, нажмите Download Zip, скачайте файл архивом.

![image_2025-01-14_12-56-26](https://github.com/user-attachments/assets/96d52781-c9a8-4233-a2e0-ae8282999a64)

Папка загрузится в формате zip, распакуйте папку с файлами, выбрав [ Извлечь в текущую папку ]

![image_2025-01-14_13-00-25](https://github.com/user-attachments/assets/d2b4b96c-ad0c-48bd-9c92-9a727b128c01)

После распаковки, папка с файлами станет доступной для её использования в Visual code, выберите [Открыть с помощью Code ]

![image_2025-01-14_13-03-22](https://github.com/user-attachments/assets/8c96c8b6-0060-4403-9641-0811935097f8)

В Visual Code откроется панель со всеми файлами с папки,для запуска кода необходимо запустить Terminal.
Перейдите как на фотографии в Terminal и выберите [ New terminal ].

![image_2025-01-14_13-14-43](https://github.com/user-attachments/assets/596148d6-3556-43f0-bf49-4ae45b9cff69)

Terminal готов для использования, теперь нам нужно создать виртуальное окружение, активировать его и установить зависимоти. Для этого в Visual Studio выполните следующие команды:

python -m venv venv 

venv\Scripts\activate.bat 

python.exe -m pip install --upgrade pip 

pip install -r requirements.txt

Для запуска бота пишем в терминале python main.py

![IMG_8351](https://github.com/user-attachments/assets/1ab35956-0603-407d-b5e9-5e0b0b3aa9ea)

![IMG_8352](https://github.com/user-attachments/assets/ddeea4f4-c908-40a4-94d8-27c7068a1267)

# Выявленные инсайты:
1. Метрика качества: Позволяет определить лучшее предложение с точки зрения цены и отзывов.
2. Популярные категории: Категории с наибольшим числом запросов у пользователей.
3. Оптимизация запросов: Использование многопоточной обработки позволило ускорить проверку изображений и снизить нагрузку на сервер.
# Ошибки:
1. Ошибка: f-string: unmatched '{'
Описание: Неправильный синтаксис строки в файле categories_key.py.
Причина: Пропущена закрывающая фигурная скобка {} в f-string.
Решение:
Было:
markup.button(text=row['name'], callback_data=f'select:{row['id']}')
Исправлено:
markup.button(text=row['name'], callback_data=f"select:{row['id']}")

2. Ошибка: ImportError: cannot import name 'categories_key'
Описание: Бот не может импортировать модуль categories_key из папки keyboard.
Причина: Путь импорта неверный или отсутствует файл __init__.py.
Решение:
Проверьте, есть ли файлing: unmatpy в папке keyboard. Если его нет, создайте пустой файл.
Проверьте правильность импорта в файле bot_commands.py:
from keyboard import categories_key

3. Ошибка: ModuleNotFoundError: No module named 'dotenv'
Описание: Библиотека python-dotenv не установлена.
Причина: Зависимость отсутствует в виртуальном окружении.
Решение:
Установите библиотеку:
pip install python-dotenv

Убедитесь, что она указана в requirements.txt:
python-dotenv~=1.0.1

4. Ошибка: FileNotFoundError: wildberries_menu.csv
Описание: Файл wildberries_menu.csv не найден.
Причина: Файл отсутствует, не создан или находится не в той директории.
Решение:
Проверьте, вызвана ли функция Parser.get_server_menu() в bot_startup.py. Она создает этот файл.
Убедитесь, что у бота есть доступ к записи в текущую директорию.
Если файл не создается, проверьте код в Parser.py и правильность URL API Wildberries:
url = 'https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v3.json'
