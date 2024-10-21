import pytest

from src.generator.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 1,
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
    {
        "id": 2,
        "operationAmount": {
            "currency": {"code": "RUB"}
        }
    },
    {
        "id": 3,
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    }
]


def test_filter_by_currency_usd():
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_empty():
    empty_transactions = filter_by_currency(transactions, "EUR")
    result = list(empty_transactions)
    assert result == []


transactions_with_descriptions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Оплата услуг"},
]


def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions_with_descriptions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Оплата услуг"


def test_transaction_descriptions_empty():
    empty_descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_descriptions)


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_range():
    generator = card_number_generator(9999999999999997, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"
