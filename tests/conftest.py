import pytest


@pytest.fixture
def card() -> str:
    return "2456856384689354"


@pytest.fixture
def account() -> str:
    return "12345456367898765432"


@pytest.fixture
def date() -> str:
    return "2024-12-06T02:26:18.671407"


@pytest.fixture
def list_of_banking_transactions() -> list[dict]:  # входящий список для сортировки для тестов
    return [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def list_of_banking_transactions_no_state() -> list[dict]:
    '''Список на ввод для теста без 'state' (значение по умолчанию) или вообще с его отсуттсвием в словаре'''
    return [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 414288290, 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def date_decreasing() -> list[dict]:  # вывод сортировки в порядке убывания - по умолчанию
    return [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def date_increasing() -> list[dict]:  # вывод сортировки в порядке возрастания
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def date_same() -> list[dict]:  # вывод сортировки при одинаковых датах на входе
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2024-12-21T21:27:25.241689'},
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2024-12-21T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2024-12-21T08:21:33.419441'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2024-12-21T02:08:58.425572'}
    ]
