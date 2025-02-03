import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_banking_transactions: list[dict]) -> None:
    '''Тестирование фильтрации списка словарей по статусу state по умолчанию "EXECUTED'''

    assert filter_by_state(list_of_banking_transactions)


def test_filter_by_state_set(list_of_banking_transactions: list[dict]) -> None:
    '''Тестирование фильтрации списка словарей по заданному статусу state CANCELED'''

    assert filter_by_state(list_of_banking_transactions, state="CANCELED")


def test_filter_by_no_state(list_of_banking_transactions_no_state: list[dict]) -> None:
    '''Проверка работы функции при отсутствии словарей с указанным статусом state в списке'''

    assert filter_by_state(list_of_banking_transactions_no_state, 'CANCELED') == []


@pytest.mark.parametrize("expected", [
    ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])
def test_filter_by_state_parametrize(list_of_banking_transactions: list[dict], expected: list[dict]) -> None:
    assert filter_by_state(list_of_banking_transactions, state='CANCELED') == expected


def test_sort_by_date_decreasing(list_of_banking_transactions: list[dict], date_decreasing: list[dict]) -> None:
    '''Тестирование сортировки списка словарей по датам в порядке убывания - по умолчанию'''

    assert sort_by_date(list_of_banking_transactions) == date_decreasing


def test_sort_by_date_increasing(list_of_banking_transactions: list[dict],
                                 date_increasing: list[dict], date: bool = False) -> None:
    '''Тестирование сортировки списка словарей по датам в порядке возрастания'''

    assert sort_by_date(list_of_banking_transactions, date=False) == date_increasing


# def test_sort_by_date_error_1() -> None:
#     '''Тест на работу функции с некорректными или нестандартными форматами дат'''
#     with pytest.raises(ValueError):
#         assert sort_by_date(
#             [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18'}]
#         ) == "Неизвестный формат даты"


# def test_sort_by_date_error_2() -> None:
#     '''Тест на работу функции с некорректными или нестандартными форматами дат'''
#     with pytest.raises(ValueError):
#         assert sort_by_date(
#             [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019'}]
#         ) == "Неизвестный формат даты"
