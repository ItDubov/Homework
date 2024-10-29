import re
from collections import defaultdict


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
    """
    Подсчитывает количество транзакций по категориям.

    :param transactions: Список словарей с транзакциями.
    :param categories: Список категорий для подсчета.
    :return: Словарь с количеством транзакций в каждой категории.
    """
    category_count = defaultdict(int)
    for tx in transactions:
        description = tx.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
                break  # Предполагаем, что одна транзакция относится к одной категории
    return dict(category_count)
