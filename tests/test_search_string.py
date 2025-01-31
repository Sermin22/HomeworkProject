import pytest
from src.search_string import search_string_in_operations


@pytest.mark.parametrize("expected", [
    ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
        'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
        'to': 'Счет 11776614605963066702'}])
])
def test_search_string_in_operations(transactions, expected):
    '''Тест проверяющий, если поисковое слово найдено и возвращена операция содержащая
    поисковую строку'''

    result = search_string_in_operations(transactions, "939719570")
    assert result == expected


def test_search_no_string_in_operations(transactions):
    '''Тест проверяющий, если поисковое слово не найдено и возвращено сообщение,
    уведомляющее об этом'''

    result = search_string_in_operations(transactions, "EUR")
    assert result == "Не найдено ни одной транзакции, подходящей под ваш поиск"
