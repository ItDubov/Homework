import os
import re
from src.api.external_api import convert_to_rub
from src.api.utils import load_transactions
from src.generator.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing.processing import filter_by_state, sort_by_date


def extract_card_number(card_info: str) -> str:
    """Извлекает номер карты из строки с информацией о карте."""
    match = re.search(r'\d{16}', card_info)
    if match:
        return match.group(0)
    else:
        raise ValueError("Номер карты не найден")


def extract_account_number(account_info: str) -> str:
    """Извлекает номер счета из строки с информацией о счете."""
    match = re.search(r'\d{20}', account_info)
    if match:
        return match.group(0)
    else:
        raise ValueError("Номер счета не найден")


def main() -> None:
    """
    Основная функция для демонстрации работы различных функций:
    маскирования, фильтрации и сортировки данных.
    """
    # Указываем путь к файлу с транзакциями
    file_path = os.path.join("data", "operations.json")

    # Загружаем транзакции из JSON-файла
    transactions = load_transactions(file_path)
    if not transactions:
        print("Ошибка: Транзакции не найдены или файл пустой.")
        return

    # Вывод информации о транзакциях
    print("Информация о транзакциях:")
    for transaction in transactions:
        transaction_id = transaction.get('id', 'Неизвестный ID')

        # Получаем дату и время
        transaction_date = transaction.get('date', 'Дата не указана')

        # Получаем номер карты отправителя
        masked_from = "Ошибка"
        if 'from' in transaction:
            try:
                card_number = extract_card_number(transaction['from'])
                masked_from = get_mask_card_number(card_number)
            except ValueError as e:
                print(f"Ошибка маскировки карты отправителя для транзакции {transaction_id}: {e}")

        # Получаем номер счета получателя
        masked_to = "Ошибка"
        if 'to' in transaction:
            try:
                account_number = extract_account_number(transaction['to'])
                masked_to = get_mask_account(account_number)
            except ValueError as e:
                print(f"Ошибка маскировки счета получателя для транзакции {transaction_id}: {e}")

        # Конвертация суммы в рубли
        amount_in_rub = None
        original_amount = None
        currency_code = None

        if "operationAmount" in transaction:
            amount_info = transaction["operationAmount"]
            if "amount" in amount_info and "currency" in amount_info:
                original_amount = float(amount_info["amount"])  # Преобразование строки в float
                currency_code = amount_info["currency"]["code"]

                # Конвертация в рубли
                try:
                    amount_in_rub = convert_to_rub({"amount": original_amount, "currency": currency_code})
                except Exception as e:
                    print(f"Ошибка при конвертации суммы для транзакции {transaction_id}: {e}")

        # Формирование вывода
        if amount_in_rub is not None:
            print(f"Транзакция ID: {transaction_id}, Дата: {transaction_date}, "
                  f"Отправитель: {masked_from}, Получатель: {masked_to}, "
                  f"Сумма: {original_amount:.2f} {currency_code} ({amount_in_rub:.2f} RUB)")
        else:
            if original_amount is not None and currency_code is not None:
                print(f"Транзакция ID: {transaction_id}, Дата: {transaction_date}, "
                      f"Отправитель: {masked_from}, Получатель: {masked_to}, "
                      f"Сумма: Конвертация не удалась. Оригинальная сумма: {original_amount:.2f} {currency_code}.")
            else:
                print(f"Транзакция ID: {transaction_id}, Дата: {transaction_date}, "
                      f"Отправитель: {masked_from}, Получатель: {masked_to}, "
                      f"Сумма: Не указана.")

if __name__ == "__main__":
    main()
