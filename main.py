from src.masks import get_mask_card_number, get_mask_account

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
        account_number = 12345678
        masked_account = get_mask_account(account_number)
        print(f"Маскированный номер счета: {masked_account}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
