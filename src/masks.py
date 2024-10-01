def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты по правилу XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа
    :return: Маскированный номер карты в виде строки
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера счета по правилу **XXXX.

    :param account_number: Номер счета в виде числа
    :return: Маскированный номер счета в виде строки
    """
    account_str = str(account_number)
    if len(account_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр.")
    return f"{account_str[:6]}** **** **** {account_str[-4:]}"
