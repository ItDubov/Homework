import re
from collections import Counter


def filter_transactions_by_description(transactions, search_str):
    """
    Фильтрует транзакции по строке в описании.

    :param transactions: Список словарей с транзакциями.
    :param search_str: Строка поиска в описании транзакций.
    :return: Список транзакций, содержащих строку поиска в описании.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx.get("description", ""))]


def count_transactions_by_category(transactions, categories):
    """Подсчитывает количество операций по категориям.

    Args:
        transactions (list): Список транзакций (словарей).
        categories (list): Список категорий для подсчета.

    Returns:
        dict: Словарь вида {"категория": количество операций}.
    """
    category_counter = Counter(
        tx.get("description", "") for tx in transactions if tx.get("description", "") in categories
    )
    return dict(category_counter)

def filter_transactions_by_status(transactions, status):
    """Фильтрует транзакции по заданному статусу, независимо от регистра.

    Args:
        transactions (list): Список транзакций (словарей).
        status (str): Статус, по которому выполняется фильтрация.

    Returns:
        list: Список транзакций, отфильтрованных по статусу.
    """
    normalized_status = status.upper()
    return [tx for tx in transactions if tx.get("status", "").upper() == normalized_status]
