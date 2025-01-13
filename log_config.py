import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Логирование в консоль
        logging.FileHandler('bot.log')  # Логирование в файл
    ])