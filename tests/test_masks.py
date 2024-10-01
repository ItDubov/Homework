import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget.mask_account_card import mask_account_card

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
