import logging
import os

# Настройка логгера для модуля masks
logger = logging.getLogger('masks_logger')
logger.setLevel(logging.DEBUG)

# Настройка file_handler для записи логов в файл
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = logging.FileHandler(os.path.join(log_dir, 'masks.log'), mode='w')
file_handler.setLevel(logging.DEBUG)

# Настройка форматера для логгера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number):
    try:
        if len(str(card_number)) != 16:
            raise ValueError("Некорректный номер карты")
        masked_number = f"{str(card_number)[:4]} **** **** {str(card_number)[-4:]}"
        logger.info(f"Успешное маскирование карты: {masked_number}")
        return masked_number
    except ValueError as e:
        logger.error(f"Ошибка в get_mask_card_number: {e}")
        raise


def get_mask_account(account_number):
    try:
        if len(str(account_number)) != 20:
            raise ValueError("Некорректный номер счета")
        masked_account = f"{str(account_number)[:4]} **** **** **** {str(account_number)[-4:]}"
        logger.info(f"Успешное маскирование счета: {masked_account}")
        return masked_account
    except ValueError as e:
        logger.error(f"Ошибка в get_mask_account: {e}")
        raise
