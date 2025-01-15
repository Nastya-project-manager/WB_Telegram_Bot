# WB_Telegram_Bot
Telegram bot для анализа товаров в WB
Наш проект представляет собой Telegram-бот, предназначенный для поиска лучших предложений на платформе Wildberries. Бот анализирует товары в различных категориях, которые мы ему прописали в файле wildberries_menu.csv на основе данных с сайта, определяет их качество и стоимость на основе отзывов, рейтингов и средней цены, а также предоставляет пользователям ссылки и изображения товаров.
# Основные функции:
1. Категории товаров: Возможность выбрать категорию товара из предостановленного списка, который появляется, когда пользователь нажимает start.
2. Анализ качества товара: Расчет метрики качества на основе рейтинга, количества отзывов и средней цены.
![Иллюстрация к проекту](https://github.com/Nadya-hope20/WB_Telegram_Bot/raw/main/main/image.png)
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
Скачайте проект с репозитория GitHub .

Зайдите в  проект в github и нажмите на кнопку Code,как указано на фотографии,нажмите Download Zip,скачайте файл архивом.

Папка загрузится в формате zip, распакуйте папку с файлами,выбрав [ Извлечь в текущую папку ]

После распаковки,папка с файлами станет доступной для её использования в Visual code,выберите [Открыть с помощью Code ]

В Visual Code откроется панель со всеми файлами с папки,для запуска кода необходимо запустить Terminal.
Перейдите как на фотографии в Terminal и выберите [ New terminal ].

Terminal готов для использования,теперь нам нужно создать виртуальное окружение ,для этого мы пишем код поэтапно для запуска

Шаг 2: Создание виртуального окружения

1.Создайте виртуальное окружение :

python -m venv venv

2.Активируйте окружение:

На Windows:
venv\Scripts\activate

На macOS/Linux:
source venv/bin/activate

Шаг 3: Установка зависимостей

Убедитесь, что файл requirements.txt находится в корне проекта.

Установите файл:

pip install -r requirements.txt

Шаг 4: Создание файла .env

В корне проекта создайте файл .env.
Добавьте в него токен бота:

BOT_TOKEN='6942271144:AAEZV2FAYl39YFPiEW_yDjvd7aI5Unzpxos'

{Получить токен можно через BotFather в Telegram.}

Запуск бота 

Убедитесь, что виртуальное окружение активировано.
Запустите проект:

python main.py

# Выявленные инсайты:
1. Метрика качества: Позволяет определить лучшее предложение с точки зрения цены и отзывов.
2. Популярные категории: Категории с наибольшим числом запросов у пользователей.
3. Оптимизация запросов: Использование многопоточной обработки позволило ускорить проверку изображений и снизить нагрузку на сервер.
