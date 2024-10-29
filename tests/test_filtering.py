from src.filterings.filtering import filter_transactions_by_description, count_transactions_by_category


def test_filter_transactions_by_description():
    transactions = [{'description': 'Оплата услуг'}, {'description': 'Открытие вклада'}]
    result = filter_transactions_by_description(transactions, 'вклад')
    assert len(result) == 1


def test_count_transactions_by_category():
    transactions = [{'description': 'Перевод'}, {'description': 'Оплата'}, {'description': 'Перевод'}]
    categories = {'Перевод': 0, 'Оплата': 0}
    result = count_transactions_by_category(transactions, categories)
    assert result == {'Перевод': 2, 'Оплата': 1}
