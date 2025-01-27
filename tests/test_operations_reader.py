import unittest
from unittest.mock import patch, mock_open
import pandas as pd
import csv
from src.operations_reader import get_data_from_excel, read_csv_dict_reader


@patch('pandas.read_excel')
def test_get_data_from_excel(mock_read_excel):
    '''Тесты для функции считывания финансовых операций из Excel c использованием patch'''

    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "Name": ["Sarah", "Mark", "John"]})
    mock_read_excel.return_value = mock_data

    result = get_data_from_excel("path_to_file")
    expected = [
        {"id": "1", "Name": "Sarah"},
        {"id": "2", "Name": "Mark"},
        {"id": "3", "Name": "John"},
    ]
    assert result == expected


def test_read_csv_dict_reader():
    '''Тесты для функции считывания финансовых операций из CSV c использованием mock_open'''
    # Данные для имитации содержимого CSV-файла
    mock_csv_data = 'id;state;date\n650703;EXECUTED;2023-09-05'

    # Используем patch для замены open на mock_open
    with patch('builtins.open', mock_open(read_data=mock_csv_data)):
        with open('file.csv', 'r') as file:
            result = read_csv_dict_reader(file)
            # Ожидаемый результат
            expected_result = [{
                'id': '650703',
                'state': 'EXECUTED',
                'date': '2023-09-05'
            }]
            # Проверяем, что результат соответствует ожидаемому
            assert result == expected_result


class TestCSVReader(unittest.TestCase):
    def test_read_csv_dict_reader(self):
        # Данные для имитации содержимого CSV-файла
        mock_csv_data = """id,state,date
650703,EXECUTED,2023-09-05T11:30:32Z
"""

        # Используем patch для замены open на mock_open
        with patch('builtins.open', mock_open(read_data=mock_csv_data)):
            with open('fake_file.csv', 'r') as file:
                reader = csv.DictReader(file)
                result = list(reader)

        # Проверяем, что результат соответствует ожидаемому
        expected_result = [{
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
        }]
        self.assertEqual(result, expected_result)
