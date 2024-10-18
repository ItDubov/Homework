import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.apilayer.com/exchangerates_data/convert"

if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с транзакцией.
    :return: Сумма в рублях (float).
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if not amount or not currency:
        raise ValueError("Transaction must include 'amount' and 'currency' fields.")

    if currency == "RUB":
        return float(amount)

    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }

    headers = {"apikey": API_KEY}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Поднимет ошибку, если статус код не 200
        data = response.json()
        print(f"API response: {data}")  # Отладочный вывод ответа
        return data.get("result", 0.0)
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return 0.0
