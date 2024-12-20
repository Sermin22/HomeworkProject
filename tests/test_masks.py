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
    ([]),
    ({"card": 3456787566}),
    ({}),
    (False),
    (3,),
    (2564569865.456)
])
def test_get_mask_card_number_wrong_type(card_number: str) -> None:
    """Функция проверяет переданный тип данных. Если параметры переданы не str,
    то вызывает исключение"""

    with pytest.raises(TypeError):
        assert get_mask_card_number(card_number) == "Ошибка типа данных"


@pytest.mark.parametrize("account_number, expected", [
    ("25645645699865325698", "**5698"),
    ("24568564567384689354", "**9354"),
    ("12340023567898765432", "**5432")
])
def test_get_mask_account_correct(account_number: str, expected: str) -> None:
    """Тестирование правильности маскирования номера счета"""

    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("25645645699", "Введен неправильный номер счета"),
    ("245685645673846893540000000", "Введен неправильный номер счета"),
    ("20символовrtyuip@@##", "Введен неправильный номер счета"),
    ("", "Введен неправильный номер счета")
])
def test_get_mask_account_len(account_number: str, expected: str) -> None:
    """Проверка на длину номера счета, на нестандартный номер (если состоит не из цифр),
    и что функция корректно обрабатывает входные строки, где отсутствует номер счета."""

    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [
    (25645698653256981234567),
    (24568563846893540000),
    ([]),
    ({}),
    ({"card": 3456787566}),
    (False),
    (3,),
    (2564569865.456)
])
def test_get_mask_account_wrong_type(account_number: str) -> None:
    """Функция проверяет переданный тип данных. Если параметры переданы не str,
    то вызывает исключение"""

    with pytest.raises(TypeError):
        assert get_mask_account(account_number) == "Ошибка типа данных"
