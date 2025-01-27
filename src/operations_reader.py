import pandas as pd
import csv


def get_data_from_excel(path_to_excel_file: str) -> list[dict]:
    """Преобразует данные из excel файла в список словарей Python"""

    data_dict = pd.read_excel(path_to_excel_file).to_dict(orient='records')
    return data_dict


def read_csv_dict_reader(filename):
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        data = list(reader)
    return data


# if __name__ == '__main__':
#     print(get_data_from_excel('transactions_excel.xlsx'))
#     print(read_csv_dict_reader('transactions.csv'))
