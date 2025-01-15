# WB_Telegram_Bot
Telegram bot для анализа товаров в WB
Наш проект представляет собой Telegram-бот, предназначенный для поиска лучших предложений на платформе Wildberries. Бот анализирует товары в различных категориях, которые мы ему прописали в файле wildberries_menu.csv на основе данных с сайта, определяет их качество и стоимость на основе отзывов, рейтингов и средней цены, а также предоставляет пользователям ссылки и изображения товаров.
Основные функции:
1. Категории товаров: Возможность выбрать категорию товара из предостановленного списка, который появляется, когда пользователь нажимает start.
2. Анализ качества товара: Расчет метрики качества на основе рейтинга, количества отзывов и средней цены. 
3. Предоставление информации о товарах: Название, цвет, бренд, рейтинг, отзывы, средняя цена, метрика качества и изображение.
4. Уведомления об ошибках: Логирование критических ошибок с уведомлением администратора.
5. Интуитивно понятный интерфейс: Бот имеет удобную навигацию через inline-кнопки.
Описание модулей:
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
Выявленные инсайты:
1. Метрика качества: Позволяет определить лучшее предложение с точки зрения цены и отзывов.
2. Популярные категории: Категории с наибольшим числом запросов у пользователей.
3. Оптимизация запросов: Использование многопоточной обработки позволило ускорить проверку изображений и снизить нагрузку на сервер.
