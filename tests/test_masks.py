import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("2564569865325698", "2564 56** **** 5698"),
    ("2456856384689354", "2456 85** **** 9354"),
    ("1234567898765432", "1234 56** **** 5432")
])
def test_get_mask_card_number_correct(card_number: str, expected: str) -> None:
    """Тестирование правильности маскирования номера карты"""

    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, expected", [
    ("2564569865", "Введен неправильный номер карты"),
    ("24568563846893540000", "Введен неправильный номер карты"),
    ("16символовrtyuip", "Введен неправильный номер карты"),
    ("", "Введен неправильный номер карты")
])
def test_get_mask_card_number_len(card_number: str, expected: str) -> None:
    """Проверка на длину номера карты, на нестандартный номер (если состоит не из цифр),
    и что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [
    (2564569865325698),
    (24568563846893540000),
    (2564569865)
])
def test_get_mask_card_number_wrong_type(card_number: str) -> None:
    """Функция проверяет переданный тип данных. Если параметры переданы не str,
    то вызывает исключение"""
    with pytest.raises(TypeError):
        assert get_mask_card_number(card_number)


# Введите номер счета: 56245689756254265897
# **5897
