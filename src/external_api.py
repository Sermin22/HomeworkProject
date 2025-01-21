import os
from dotenv import load_dotenv
import requests
from src.utils import list_financial_transactions


def conversion_to_rubles(transactions: list[dict]) -> list:
    '''Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего
    курса валют и конвертации суммы операции в рубли.'''

    list_amount = []
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                amount_rub = float(transaction["operationAmount"]["amount"])
                list_amount.append(amount_rub)
            if transaction["operationAmount"]["currency"]["code"] != "RUB":
                from_code = transaction["operationAmount"]["currency"]["code"]  # Трехбуквенный код валюты,
                # которую вы хотите конвертировать
                to = "RUB"  # Трехбуквенный код валюты, в которую вы хотите конвертировать
                amount = float(transaction["operationAmount"]["amount"])  # Сумма, подлежащая конвертации
                load_dotenv()
                APIlayer_KEY = os.getenv('APIlayer_KEY')
                headers = {
                    "apikey": APIlayer_KEY
                }
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_code}&amount={amount}"
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    result = response.json()['result']
                    result = round(float(result), 4)
                    list_amount.append(result)
                else:
                    print(f"Конвертация валюты неуспешна. Возможная причина: {response.reason}")
        except KeyError:
            continue
    return list_amount


# if __name__ == "__main__":
#     transactions = list_financial_transactions("../data/transactions.json")
#     print(conversion_to_rubles(transactions))

    # print(conversion_to_rubles([{"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}},
    #                 {"operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}}}]))

    # print(conversion_to_rubles([{"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}]))
