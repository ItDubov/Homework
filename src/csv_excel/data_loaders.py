import pandas as pd
import json


def load_transactions_from_json(operations_json_file: str):
    try:
        with open(operations_json_file, encoding="utf-8") as f:
            transactions = json.load(f)
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении JSON: {e}")
        return []


def load_transactions_from_csv(transactions_file: str):
    """Загружает транзакции из CSV-файла."""
    try:
        data = pd.read_csv(transactions_file)
        return data.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def load_transactions_from_excel(transactions_excel_file: str):
    """Загружает транзакции из Excel-файла."""
    try:
        data = pd.read_excel(transactions_excel_file)
        return data.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
