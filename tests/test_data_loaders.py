from unittest.mock import patch
import pandas as pd
from csv_excel.data_loaders import load_transactions_from_csv


@patch("pandas.read_csv")
def test_load_transactions_from_csv(mock_read_csv):
    # Создаем фиктивные данные
    mock_data = pd.DataFrame({"id": [1], "amount": [100], "currency": ["USD"]})
    mock_read_csv.return_value = mock_data

    transactions = load_transactions_from_csv("test.csv")
    assert transactions == [{"id": 1, "amount": 100, "currency": "USD"}]
