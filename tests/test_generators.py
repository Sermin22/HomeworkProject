import pytest
from typing import Iterator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize("expected", [
    ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
       'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
       'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
      {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
       'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
       'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
       'to': 'Счет 75651667383060284188'}])
])
def test_filter_by_currency(transactions: list[dict], expected: Iterator[dict]) -> None:
    """Тест на проверку, что функция корректно фильтрует транзакции по заданной валюте"""

    usd_transactions = filter_by_currency(transactions, "USD")
    for exp in expected:
        assert next(usd_transactions, "StopIteration") == exp


def test_filter_by_currency_no_code(transactions: list[dict]) -> None:
    """Тест на проверку, что функция правильно обрабатывает случаи, когда транзакции в заданной
    валюте отсутствуют или в списке нет соответствующих валютных операций"""

    usd_transactions = filter_by_currency(transactions, "JPY")

    assert next(usd_transactions, "StopIteration")


def test_filter_by_currency_empty_list(transactions: list[dict]) -> None:
    """Тест на проверку, что что генератор не завершается ошибкой при обработке пустого списка"""

    usd_transactions = filter_by_currency([], "USD")

    assert next(usd_transactions, "StopIteration")


@pytest.mark.parametrize("expected", [
    (["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
      "Перевод с карты на карту", "Перевод организации"])
])
def test_transaction_descriptions(transactions: list[dict], expected: str) -> None:
    """Тест на проверку, что функция возвращает корректные описания для каждой транзакции."""

    descriptions = transaction_descriptions(transactions)
    for exp in expected:
        assert next(descriptions) == exp


def test_transaction_descriptions_empty_list(transactions: list[dict]) -> None:
    """Тест на проверку, что функция работает с пустым списком."""

    descriptions = transaction_descriptions([])

    assert next(descriptions, "StopIteration")


def test_transaction_descriptions_empty_descriptions(transactions: list[dict]) -> None:
    """Тест на проверку, что функция работает с пустым description."""

    descriptions = transaction_descriptions([{"id": 939719570, "state": "EXECUTED",
                                              "date": "2018-06-30T02:08:58.425572",
                                              "operationAmount": "9824.07", "description": ""}])

    assert next(descriptions, "StopIteration") == ""


@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003",
            "0000 0000 0000 0004", "0000 0000 0000 0005"]),

])
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    """Тест на проверку, что генератор выдает правильные номера карт в заданном диапазоне и
корректно форматирует номера карт"""

    card_number = card_number_generator(start, stop)
    for exp in expected:
        assert next(card_number) == exp


@pytest.mark.parametrize("start, stop, expected", [
    (10000000000000000, 10000000000000000, "Задан неверный  диапазон номера карты"),
    (-1, 2, "Задан неверный диапазон номера карты")
])
def test_card_number_generator_extreme_values(start: int, stop: int, expected: str) -> None:
    """Тест на проверку, что генератор возвращает исключение если неверно указан диапазон
    номеров (отрицательные или числа свыше 16 цифр)"""

    with pytest.raises(ValueError):
        card_number = card_number_generator(start, stop)
        assert next(card_number) == expected
