from typing import List, Dict, Optional


def filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по указанному состоянию.

    :param data: Список словарей с банковскими операциями
    :param state: Состояние, по которому фильтруем (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список операций
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param data: Список словарей с банковскими операциями
    :param reverse: Порядок сортировки (по умолчанию True — убывание)
    :return: Отсортированный список операций
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
