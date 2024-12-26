import pytest
from typing import Iterator
from src.generators import filter_by_currency


@pytest.mark.parametrize("expected", [
    ({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
      'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
      'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'})
])
def test_filter_by_currency(transactions: list[dict], expected: Iterator[dict]) -> None:
    """Тесты на проверку, что функция корректно фильтрует транзакции по заданной валюте"""
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(1):
        assert (next(usd_transactions)) == expected
