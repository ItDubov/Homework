import pytest
from src.processing.processing import filter_by_state, sort_by_date

# Фикстура для тестовых данных
@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-09-29T14:33:21.123456'},
        {'id': 2, 'state': 'CANCELED', 'date': '2022-10-12T09:12:47.789456'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2021-07-15T17:29:31.654321'}
    ]

# Тесты для функции filter_by_state
def test_filter_by_state_default(sample_data):
    filtered = filter_by_state(sample_data)
    assert len(filtered) == 2
    assert all(item['state'] == 'EXECUTED' for item in filtered)

def test_filter_by_state_canceled(sample_data):
    filtered = filter_by_state(sample_data, 'CANCELED')
    assert len(filtered) == 1
    assert filtered[0]['state'] == 'CANCELED'

# Тесты для функции sort_by_date
def test_sort_by_date_desc(sample_data):
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]['date'] == '2023-09-29T14:33:21.123456'

def test_sort_by_date_asc(sample_data):
    sorted_data = sort_by_date(sample_data, reverse=False)
    assert sorted_data[0]['date'] == '2021-07-15T17:29:31.654321'
