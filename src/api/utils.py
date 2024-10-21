import json
import logging
import os

# Настройка логгера для модуля utils
logger = logging.getLogger('utils_logger')
logger.setLevel(logging.DEBUG)

# Настройка file_handler для записи логов в файл
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = logging.FileHandler(os.path.join(log_dir, 'utils.log'), mode='w')
file_handler.setLevel(logging.DEBUG)

# Настройка форматера для логгера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                logger.error(f"Файл {file_path} не содержит список транзакций")
                return []
            logger.info(f"Успешная загрузка данных из {file_path}")
            return data
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}")
        return []
