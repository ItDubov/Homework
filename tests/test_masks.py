import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget.mask_account_card import get_date, mask_account_card


# Фикстура для тестирования
@pytest.fixture
def card_number():
    return "1234567812345678"


@pytest.fixture
def account_number():
    return "12345678901234567890"


# Тесты для функции get_mask_card_number
def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError):
        get_mask_card_number("")


# Тесты для функции get_mask_account
def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "123456** **** **** 7890"


def test_get_mask_account_short():
    with pytest.raises(ValueError):
        get_mask_account("1234")


# Тесты для функции mask_account_card
def test_mask_account_card_card_info():
    assert mask_account_card("Visa 1234567812345678") == "Visa 1234 56** **** 5678"


def test_mask_account_card_account_info():
    assert mask_account_card("Счет 12345678901234567890") == "Счет 123456** **** **** 7890"


def test_mask_account_card_invalid_data():
    with pytest.raises(ValueError):
        mask_account_card("Некорректные данные")


def test_get_date():
    # Тест правильного формата даты
    date_str = "2024-03-11T02:26:18.671407"
    assert get_date(date_str) == "11.03.2024"

    # Тест некорректного формата даты
    with pytest.raises(ValueError):
        get_date("некорректная_дата")
