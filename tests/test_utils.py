import pytest

from src.api.utils import load_transactions


def test_load_transactions_file_not_found():
    assert load_transactions("invalid_path.json") == []


def test_load_transactions_invalid_format(tmpdir):
    # Создание временного файла с некорректными данными
    file = tmpdir.join("test.json")
    file.write('{"invalid": "data"}')

    assert load_transactions(file.strpath) == []


def test_load_transactions_valid(tmpdir):
    # Создание временного файла с корректными данными
    file = tmpdir.join("test.json")
    file.write('[{"amount": 100, "currency": "RUB"}]')

    assert load_transactions(file.strpath) == [{"amount": 100, "currency": "RUB"}]
