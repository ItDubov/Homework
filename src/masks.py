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
        card_number_str = str(card_number).replace(" ", "").replace("-", "")  # Удаление пробелов и дефисов
        if len(card_number_str) != 16:
            raise ValueError("Некорректный номер карты, длина должна быть 16 символов")
        masked_number = f"{card_number_str[:4]} **** **** {card_number_str[-4:]}"
        logger.info(f"Успешное маскирование карты: {masked_number}")
        return masked_number
    except ValueError as e:
        logger.error(f"Ошибка в get_mask_card_number для {card_number}: {e}")
        raise
    except Exception as e:
        logger.exception("Неизвестная ошибка в get_mask_card_number")
        raise


def get_mask_account(account_number):
    try:
        account_number_str = str(account_number).replace(" ", "")  # Удаление пробелов
        if len(account_number_str) != 20:
            raise ValueError("Некорректный номер счета, длина должна быть 20 символов")
        masked_account = f"{account_number_str[:4]} **** **** **** {account_number_str[-4:]}"
        logger.info(f"Успешное маскирование счета: {masked_account}")
        return masked_account
    except ValueError as e:
        logger.error(f"Ошибка в get_mask_account для {account_number}: {e}")
        raise
    except Exception as e:
        logger.exception("Неизвестная ошибка в get_mask_account")
        raise
