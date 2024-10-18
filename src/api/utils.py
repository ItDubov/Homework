import json
import os


def load_transactions(file_path):
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: Путь до файла с транзакциями.
    :return: Список транзакций или пустой список при ошибке.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
