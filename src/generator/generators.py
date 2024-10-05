from typing import Iterator

def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """
    Генератор, который фильтрует транзакции по валюте.

    :param transactions: Список транзакций
    :param currency_code: Код валюты для фильтрации (например, "USD")
    :return: Итератор по транзакциям с указанной валютой
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction

def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции.

    :param transactions: Список транзакций
    :return: Итератор, возвращающий описание транзакции
    """
    for transaction in transactions:
        yield transaction.get("description", "")

def card_number_generator(start: int, end: int) -> Iterator[int]:
    """
    Генератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальный номер (целое число)
    :param end: Конечный номер (целое число)
    :return: Итератор по номерам карт в заданном диапазоне
    """
    for number in range(start, end + 1):
        card_str = f"{number:016d}"  # Преобразуем число в строку из 16 цифр
        formatted_card = int(f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}")
        yield formatted_card


