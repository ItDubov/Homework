def filter_transactions_by_status(transactions, status):
    """Фильтрует транзакции по статусу, с учетом регистра."""
    normalized_status = status.upper()
    return [tx for tx in transactions if tx.get("status", "").upper() == normalized_status]


def sort_transactions_by_date(transactions, ascending=True):
    """Сортирует транзакции по дате."""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=not ascending)


def filter_transactions_by_currency(transactions, currency="RUB"):
    """Фильтрует транзакции по валюте."""
    return [tx for tx in transactions if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency]
