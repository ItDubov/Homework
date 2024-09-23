from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от переданного типа.

    :param data: Строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"
    :return: Маскированный номер карты или счета
    """
    parts = data.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат строки")

    number = parts[-1]
    card_types = ["Visa", "Maestro", "MasterCard"]

    if any(card_type in data for card_type in card_types):
        # Обрабатываем как номер карты
        if len(number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        return f"{' '.join(parts[:-1])} {get_mask_card_number(int(number))}"
    elif "Счет" in data:
        # Обрабатываем как номер счета
        if len(number) != 20:
            raise ValueError("Номер счета должен содержать 20 цифр")
        return f"{' '.join(parts[:-1])} {get_mask_account(int(number))}"
    else:
        raise ValueError("Неизвестный тип счета или карты")

from datetime import datetime

def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ.

    :param date_str: Дата в формате "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024"
    """
    date = datetime.fromisoformat(date_str)
    return date.strftime("%d.%m.%Y")
