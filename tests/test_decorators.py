import pytest

from src.decorator.decorators import log


@log()
def add(a, b):
    return a + b


@log()
def divide(a: object, b: object) -> object:
    return a / b


# Тест успешного выполнения функции add
def test_add(caplog):
    add(2, 3)
    # Проверяем, что лог содержит успешное выполнение
    assert "add ok" in caplog.text


# Тест успешного выполнения функции divide
def test_divide(caplog):
    divide(6, 3)
    # Проверяем, что лог содержит успешное выполнение
    assert "divide ok" in caplog.text


# Тест ошибки при делении на ноль
def test_divide_by_zero(caplog):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    # Проверяем, что в логе есть ошибка
    assert "divide error: ZeroDivisionError" in caplog.text
