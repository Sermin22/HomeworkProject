import pytest
from typing import Iterator
from src.generators import filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("expected", [
    ({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
      'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
      'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
      'to': 'Счет 11776614605963066702'})
])
@pytest.mark.parametrize("expected2", [
    ({'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
      'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
      'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
      'to': 'Счет 75651667383060284188'})
])
def test_filter_by_currency(transactions: list[dict], expected: Iterator[dict], expected2: Iterator[dict]) -> None:
    """Тесты на проверку, что функция корректно фильтрует транзакции по заданной валюте"""
    usd_transactions = filter_by_currency(transactions, "USD")

    assert next(usd_transactions, "StopIteration") == expected
    assert next(usd_transactions, "StopIteration") == expected2


def test_filter_by_currency_no_code(transactions: list[dict]) -> None:
    """Тесты на проверку, что функция правильно обрабатывает случаи, когда транзакции в заданной
    валюте отсутствуют или в списке нет соответствующих валютных операций"""
    usd_transactions = filter_by_currency(transactions, "JPY")

    assert next(usd_transactions, "StopIteration")
    assert next(usd_transactions, "StopIteration")


def test_filter_by_currency_empty_list(transactions: list[dict]) -> None:
    """Тесты на проверку, что что генератор не завершается ошибкой при обработке пустого списка"""
    usd_transactions = filter_by_currency([], "USD")

    assert next(usd_transactions, "StopIteration")
    assert next(usd_transactions, "StopIteration")


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """Тест на проверку, что функция возвращает корректные описания для каждой транзакции."""

    descriptions = transaction_descriptions(transactions)

    assert next(descriptions, "StopIteration") == "Перевод организации"
    assert next(descriptions, "StopIteration") == "Перевод со счета на счет"
    assert next(descriptions, "StopIteration") == "Перевод со счета на счет"
    assert next(descriptions, "StopIteration") == "Перевод с карты на карту"
    assert next(descriptions, "StopIteration") == "Перевод организации"


def test_transaction_descriptions_empty_list(transactions: list[dict]) -> None:
    """Тест на проверку, что функция работает с пустым списком."""

    descriptions = transaction_descriptions([])

    assert next(descriptions, "StopIteration")


def test_transaction_descriptions_empty_descriptions(transactions: list[dict]) -> None:
    """Тест на проверку, что функция работает с пустым scriptions."""

    descriptions = transaction_descriptions([{"id": 939719570, "state": "EXECUTED",
                                              "date": "2018-06-30T02:08:58.425572",
                                              "operationAmount": "9824.07", "description": ""}])

    assert next(descriptions, "StopIteration") == ""
