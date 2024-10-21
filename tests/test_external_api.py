from unittest.mock import patch

from src.api.external_api import convert_to_rub


@patch('src.external_api.requests.get')
def test_convert_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 75.0}
    transaction = {"amount": 1, "currency": "USD"}

    result = convert_to_rub(transaction)
    assert result == 75.0


@patch('src.external_api.requests.get')
def test_convert_to_rub_rub_currency(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}

    result = convert_to_rub(transaction)
    assert result == 100.0
