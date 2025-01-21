from unittest.mock import mock_open, patch, Mock
from src.external_api import conversion_to_rubles
from src.utils import list_financial_transactions
import pytest

def test_conversion_to_rubles():
    '''Тест функции, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float, если транзакция была в рублях с кодом RUB'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", '
                                      '"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, '
                                      '"description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывается функция, которая читает JSON-файл
        result = conversion_to_rubles(list_financial_transactions("../data/transactions.json"))
        assert result == [31957.58]


# def test_conversion_to_rubles_convert():
#     with patch('requests.get') as mock_get:
#         mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
#                                                    'info': {'timestamp': 1737394036, 'rate': 101.49124},
#                                                    'date': '2025-01-20', 'result': 834397.035799}
#         transaction = [{"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}]
#         result = conversion_to_rubles(transaction)
#         assert result == [834397.0357]
#         # result = conversion_to_rubles(list_financial_transactions("../data/transactions.json"))
#         # assert result == [834397.0357]
#         mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_code}&amount={amount}')


@pytest.fixture
def mock_exchange_rate_api():
    with patch('src.external_api.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                           'info': {'timestamp': 1737394036, 'rate': 101.49124},
                                           'date': '2025-01-20', 'result': 834397.035799}
        mock_get.return_value = mock_response
        return mock_get

def test_convert_currency(mock_exchange_rate_api):
    transaction = [{"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}]
    result = conversion_to_rubles(transaction)
    assert result == [834397.0358]


@pytest.fixture
def mock_read_json_file():
    with patch('src.utils.list_financial_transactions') as mock_read:
        mock_read.return_value = [{"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}},
                                  {"operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}}}]
        yield mock_read

def test_some_function(mock_read_json_file):
    transactions = list_financial_transactions('../data/transactions.json')
    # Тестируй свою функцию, используя mock_read_json_file
    assert len(transactions) == 4


# def test_conversion_to_rubles_convert():
#     with patch('requests.get') as mock_get:
#         res = [{'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1737394036, 'rate': 101.49124}, 'date': '2025-01-20', 'result': 834397.035799},
#                {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 9824.07}, 'info': {'timestamp': 1737394036, 'rate': 105.132989}, 'date': '2025-01-20', 'result': 1032833.843245}]
#         mock_get.return_value.json.return_value = [r for r in res]
#         result = conversion_to_rubles(mock_read_json_file)
#         assert result == [834397.0357, 1032833.8432]
#         # result = conversion_to_rubles(list_financial_transactions("../data/transactions.json"))
#         # assert result == [834397.0357]
#         mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_code}&amount={amount}')


# @patch('requests.get')
# def test_conversion_to_rubles_convert(mock_get):
#     transactions = [{"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}},
#                     {"operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}}}]
#     mock_get.return_value.json.return_value = [834361.0591, 1037087.587]
#     assert conversion_to_rubles(transactions) == [834361.0591, 1037087.587]
#     mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_code}&amount={amount}')



def test_conversion_to_rubles_convert():
    with patch('requests.get') as mock_get:
        transaction = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",
                        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации", "from": "MasterCard 7158300734726758",
                        "to": "Счет 35383033474447895560"}]
        mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1737394036, 'rate': 101.49124}, 'date': '2025-01-20', 'result': 834397.035799}
        assert conversion_to_rubles(transaction) == [834397.0357]
        mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37')

#  Это возвращает функция конвертации из API готовый вариант
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1737394036, 'rate': 101.49124}, 'date': '2025-01-20', 'result': 834397.035799}
# {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 9824.07}, 'info': {'timestamp': 1737394036, 'rate': 105.132989}, 'date': '2025-01-20', 'result': 1032833.843245}