from src.csv_excel.data_loaders import (load_transactions_from_csv,
                                        load_transactions_from_excel,
                                        load_transactions_from_json
                                        )
import src.filterings.transaction_processing as processing
from src.filterings.filtering import filter_transactions_by_description


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ")
    if choice == "1":
        transactions = load_transactions_from_json("data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = load_transactions_from_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = load_transactions_from_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран Excel-файл.")
    else:
        print("Неверный выбор.")
        return

    if not transactions:
        print("Файл транзакций пуст или не существует.")
        return

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").upper()
        if status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции '{status}' недоступен.")
            continue
        transactions = processing.filter_transactions_by_status(transactions, status)
        print(f"Операции отфильтрованы по статусу '{status}'")
        break

    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        ascending = (order_choice == "по возрастанию")
        transactions = processing.sort_transactions_by_date(transactions, ascending)

    currency_choice = input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if currency_choice == "да":
        transactions = processing.filter_transactions_by_currency(transactions, "RUB")

    search_choice = input("Отфильтровать по ключевому слову в описании? (Да/Нет): ").strip().lower()
    if search_choice == "да":
        search_str = input("Введите ключевое слово: ").strip()
        transactions = filter_transactions_by_description(transactions, search_str)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for tx in transactions:
            print(f"{tx['date']} {tx['description']}")
            print(f"{tx.get('from', '')} -> {tx.get('to', '')}")
            amount = tx.get("operationAmount", {}).get("amount")
            currency = tx.get("operationAmount", {}).get("currency", {}).get("name")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
