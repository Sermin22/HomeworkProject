import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card_card(card: str) -> None:
    '''Проверяет правильность маскировки карты'''
    assert mask_account_card(card) == " 2456 85** **** 9354"


def test_mask_account_card_account(account: str) -> None:
    '''Проверяет правильность маскировки счета'''
    assert mask_account_card(account) == " **5432"


@pytest.mark.parametrize("card_or_account_number, expected", [
    ("Maestro 2564569865325698", "Maestro 2564 56** **** 5698"),
    ("Visa 2456856384689354", "Visa 2456 85** **** 9354"),
    ("Счет 12345456367898765432", "Счет **5432"),
    ("Счет 23459875697256896248", "Счет **6248")
])
def test_mask_account_card_correct(card_or_account_number: str, expected: str) -> None:
    """Тестирование правильности маскирования номеров карт и номеров счетов"""

    assert mask_account_card(card_or_account_number) == expected


@pytest.mark.parametrize("card_or_account_number, expected", [
    ("Maestro 2564569865", ""),
    ("Счет 245685638468935400021", ""),
    ("буквыразныеrtyuip", ""),
    ("@@@@@#####%%%%%$$$$", ""),
    ("", "")
])
def test_mask_account_card_len(card_or_account_number: str, expected: str) -> None:
    """Проверка на длину номера карты или счета, на нестандартный номер (если состоит не из цифр),
    и что функция корректно обрабатывает входные строки, где отсутствует номер карты, счета."""

    assert mask_account_card(card_or_account_number) == expected


# @pytest.mark.parametrize("card_or_account_number", [
#     (2564569865325698),
#     (24568563846893540000),
#     ([]),
#     ({"card": 3456787566}),
#     ({}),
#     (False),
#     (3,),
#     (2564569865.456)
# ])
# def test_mask_account_card_wrong_type(card_or_account_number: str) -> None:
#     """Функция проверяет переданный тип данных. Если параметры переданы не str,
#     то вызывает исключение"""
#
#     with pytest.raises(TypeError):
#         assert mask_account_card(card_or_account_number) == "Ошибка типа данных"


def test_get_date(date: str) -> None:
    '''Тестирование правильности преобразования даты'''

    assert get_date(date) == "06.12.2024"


@pytest.mark.parametrize("date, expected", [
    ("2024-12-06T02:26:18.671407", "06.12.2024"),
    ("2023-10-11T0", "11.10.2023"),
    ("2024-12-21", "21.12.2024"),
    ("2024-12-6", "Неизвестный формат даты"),
    ("2024.12.06T02:26:18.671407", "Неизвестный формат даты"),
    ("20241206T02:26:18.671407", "Неизвестный формат даты"),
    ("", "Неизвестный формат даты")
])
def test_get_date_correct(date: str, expected: str) -> None:
    '''Проверка на различные входные форматы даты, включая граничные случаи
    и нестандартные строки с датами, проверка, что функция корректно обрабатывает
    входные строки, где отсутствует дата.'''

    assert get_date(date) == expected


# @pytest.mark.parametrize("date", [
#     (24568563846893540000),
#     ([]),
#     ({"card": 3456787566}),
#     ({}),
#     (False),
#     (3,),
#     (2564569865.456)
# ])
# def test_get_date_wrong_type(date: str) -> None:
#     """Функция проверяет переданный тип данных. Если параметры переданы не str,
#         то вызывает исключение"""
#
#     with pytest.raises(TypeError):
#         assert mask_account_card(date) == "Ошибка типа данных"
