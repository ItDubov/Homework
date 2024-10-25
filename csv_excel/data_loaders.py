import pandas as pd


def load_transactions_from_csv(transactions_file: str):
    """
    Считывает транзакции из CSV-файла.

    :param transactions_file: Путь к CSV-файлу с транзакциями.
    :return: Список словарей, представляющих транзакции, или пустой список в случае ошибки.
    """
    try:
        data = pd.read_csv(transactions_file)
        transactions = data.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def load_transactions_from_excel(transactions_excel_file: str):
    """
    Считывает транзакции из Excel-файла.

    :param transactions_excel_file: Путь к Excel-файлу с транзакциями.
    :return: Список словарей, представляющих транзакции, или пустой список в случае ошибки.
    """
    try:
        data = pd.read_excel(transactions_excel_file)
        transactions = data.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
