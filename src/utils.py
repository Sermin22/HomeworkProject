from typing import Any
import json


def list_financial_transactions(file_json: str) -> list[dict[Any, Any]]:
    '''Принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях'''
    try:
        with open(file_json, encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    if data and isinstance(data, list):
        return data
    else:
        return []


# if __name__ == "__main__":
#     print(list_financial_transactions("../data/transactions.json"))
