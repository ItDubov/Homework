from src.masks import get_mask_account, get_mask_card_number

from src.widget.mask_account_card import mask_account_card, get_date


def main():
    """
    Основная функция для демонстрации работы функций маскирования.
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


if __name__ == "__main__":
    main()
