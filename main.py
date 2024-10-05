from src.masks import get_mask_account, get_mask_card_number
from src.widget.mask_account_card import mask_account_card, get_date
from src.processing.processing import filter_by_state, sort_by_date
from src.generator.generators import filter_by_currency, transaction_descriptions, card_number_generator


def main():
    """
    Основная функция для демонстрации работы различных функций:
    маскирования, фильтрации и сортировки данных.
    """
    # Пример использования функции get_mask_card_number
    try:
        card_number = 1234567812345678
        masked_card = get_mask_card_number(card_number)
        print(f"Маскированный номер карты: {masked_card}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Пример использования функции get_mask_account
    try:
        account_number = 12345678901234567890
        masked_account = get_mask_account(account_number)
        print(f"Маскированный номер счета: {masked_account}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Пример использования функции mask_account_card
    try:
        card_info = "Visa Platinum 7000792289606361"
        masked_info = mask_account_card(card_info)
        print(f"Маскированная информация о карте: {masked_info}")

        account_info = "Счет 73654108430135874305"
        masked_account_info = mask_account_card(account_info)
        print(f"Маскированная информация о счете: {masked_account_info}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Пример использования функции get_date
    try:
        date_str = "2024-03-11T02:26:18.671407"
        formatted_date = get_date(date_str)
        print(f"Отформатированная дата: {formatted_date}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Демонстрация работы функций filter_by_state и sort_by_date
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    # Фильтрация по состоянию 'EXECUTED'
    filtered_data = filter_by_state(data)
    print("Фильтрация по статусу 'EXECUTED':", filtered_data)

    # Фильтрация по состоянию 'CANCELED'
    canceled_data = filter_by_state(data, 'CANCELED')
    print("Фильтрация по статусу 'CANCELED':", canceled_data)

    # Сортировка по дате (по убыванию)
    sorted_data_desc = sort_by_date(data)
    print("Сортировка по убыванию:", sorted_data_desc)

    # Сортировка по дате (по возрастанию)
    sorted_data_asc = sort_by_date(data, reverse=False)
    print("Сортировка по возрастанию:", sorted_data_asc)

    # Пример транзакций
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]

    # Использование генератора filter_by_currency
    print("USD транзакции:")
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))

    # Использование генератора transaction_descriptions
    print("\nОписания транзакций:")
    descriptions = transaction_descriptions(transactions)
    for _ in range(3):
        print(next(descriptions))

    # Использование генератора card_number_generator
    print("\nГенерация номеров карт:")
    for card_number in card_number_generator(1, 5):
        print(card_number)


if __name__ == "__main__":
    main()
