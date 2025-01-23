from unittest.mock import patch
from src.external_api import conversion_to_rubles
import pytest


@pytest.fixture
def transaction_rub():  # входные данные (параметр), для тестирования функции conversion_to_rubles
    # с "code": "RUB"
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'}]


def test_conversion_to_rubles(transaction_rub):
    '''Тест функции, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
     тип данных — float, если транзакция была в рублях с кодом RUB'''

    assert conversion_to_rubles(transaction_rub) == [31957.58]


@pytest.fixture
def transaction_usd():  # входные данные (параметр), для тестирования функции conversion_to_rubles
    # с "code": "USD"
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",
             "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации", "from": "MasterCard 7158300734726758",
             "to": "Счет 35383033474447895560"}]


def test_conversion_to_rubles_convert(transaction_usd):
    '''Тест функции, если транзакция была в USD, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли, при условии status_code = 200'''
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        result = conversion_to_rubles(transaction_usd)
        assert result == [1.0]
        mock_get.assert_called_once()


def test_conversion_to_rubles_not_convert(transaction_usd):
    '''Тест функции, если транзакция была в USD, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли, при условии status_code != 200'''
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code != 200
        result = conversion_to_rubles(transaction_usd)
        assert result == []
        mock_get.assert_called_once()


#  Ниже приведен пример ответа от конечной точки из API
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
# 'info': {'timestamp': 1737394036, 'rate': 101.49124}, 'date': '2025-01-20', 'result': 834397.035799}
# {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 9824.07},
# 'info': {'timestamp': 1737394036, 'rate': 105.132989}, 'date': '2025-01-20', 'result': 1032833.843245}
