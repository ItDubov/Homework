import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")


def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с транзакцией, должен содержать 'amount' и 'currency'.
    :return: Сумма в рублях (float).
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if not amount or not currency:
        raise ValueError("Transaction must include 'amount' and 'currency' fields.")

    # Если валюта уже рубли, просто возвращаем сумму
    if currency == "RUB":
        return float(amount)

    # Параметры запроса к API для конвертации валюты
    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }

    headers = {"apikey": API_KEY}

    try:
        # Выполняем запрос к API
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Поднимет ошибку, если статус код не 200
        data = response.json()

        # Отладочный вывод ответа API
        print(f"API response: {data}")  # Отладочный вывод ответа

        # Проверка наличия результата в ответе API
        if "result" in data:
            return data["result"]  # Возвращаем результат конвертации
        else:
            print("Ошибка: Результат не найден в ответе API.")
            return 0.0

    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return 0.0
