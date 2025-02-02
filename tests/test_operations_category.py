import pytest
from collections import Counter
from src.operations_category import number_of_operations_category


@pytest.mark.parametrize("categories, expected", [
    (["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
     {'Перевод организации': 2, 'Перевод со счета на счет': 2, 'Перевод с карты на карту': 1})
])
def test_number_of_operations_category(transactions, categories, expected):
    '''Тест корректтности работы функции, принимающей список с данными о банковских операциях
    и список категорий операций и возвращающей словарь с ключами (названия категорий),
    а значениями (количество операций в каждой категории).'''

    result = number_of_operations_category(transactions, categories)
    assert result == expected
