from typing import Any


def filter_by_state(list_of_banking_transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Принимает список словарей и значение для ключа state и возвращает новый список словарей,
    содержащий только те словари, у которых ключ соответствует указанному значению.
    """

    new_list_of_banking_transactions = []
    for banking_transactions in list_of_banking_transactions:
        if banking_transactions.get("state") == state:
            new_list_of_banking_transactions.append(banking_transactions)
    return new_list_of_banking_transactions


def sort_by_date(list_of_transaction_dates: list[dict[str, Any]], date = True):
    sorted_list_of_transaction_dates = sorted(list_of_transaction_dates, key=lambda i: i.get("date", 0), reverse=date)
    return sorted_list_of_transaction_dates


if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "CANCELED"))

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
