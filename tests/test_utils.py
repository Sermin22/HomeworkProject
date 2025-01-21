from unittest.mock import mock_open, patch
from src.utils import list_financial_transactions


def test_list_financial_transactions():
    '''Тестирование на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = list_financial_transactions("../data/transactions.json")
        assert result == [{"id": 1, "amount": "100.0"}]


def test_list_financial_transactions_empty_file():
    '''Тестирование на вход если файл пустой, то возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = list_financial_transactions("../data/transactions.json")
        assert result == []


def test_list_financial_transactions_not_found_file():
    '''Тестирование на вход если файл не найден, то возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data=None)

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = list_financial_transactions("../data/transactions.json")
        assert result == []


def test_list_financial_transactions_error():
    '''Тестирование на вход путь до JSON-файла и если JSON-строка имеет неправильный формат,
    содержит некорректные символы или имеет другие ошибки и невозможно декорировать, то обрабатывает
    исключение и возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"]')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = list_financial_transactions("../data/transactions.json")
        assert result == []


def test_list_financial_transactions_not_isinstance():
    '''Тестирование на вход путь до JSON-файла и если файл не список, то возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='{"id": 1, "amount": "100.0"}')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = list_financial_transactions("../data/transactions.json")
        assert result == []
