import os
from src.utils import list_financial_transactions
from src.operations_reader import read_csv_dict_reader, get_data_from_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.search_string import search_string_in_operations
from src.widget import get_date, mask_account_card
from src.generators import transaction_descriptions


def main() -> str:
    '''Функция отвечает за основную логику проекта с пользователем и связывает функциональности
    между собой.'''

    print("""
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла")
""")
    list_operations = []
    choice_file = input("Введите 1, 2 или 3: ")
    if choice_file == "1":
        print("Для обработки выбран JSON-файл")
        PATH_TO_FILE_JSON = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        operations_json = list_financial_transactions(PATH_TO_FILE_JSON)
        list_operations = operations_json
    elif choice_file == "2":
        print("Для обработки выбран CSV-файл")
        PATH_TO_FILE_CSV = os.path.join(os.path.dirname(__file__), "src", "transactions.csv")
        transactions_csv = read_csv_dict_reader(PATH_TO_FILE_CSV)
        list_operations = transactions_csv
    elif choice_file == "3":
        print("Для обработки выбран XLSX-файл")
        PATH_TO_FILE_XLSX = os.path.join(os.path.dirname(__file__), "src", "transactions_excel.xlsx")
        transactions_xlsx = get_data_from_excel(PATH_TO_FILE_XLSX)
        list_operations = transactions_xlsx
    else:
        print("Неверно выбран файл, повторите снова")

    print("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
    list_choice_status = ["executed", "canceled", "pending"]
    count = 0
    choice_status = input("Введите статус: ").lower()
    while choice_status not in list_choice_status:
        count += 1
        if count > 3:
            break
        choice_status = input(f"Статус операции {choice_status} недоступен.\n"
                              f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                              f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").lower()

    if choice_status not in list_choice_status:
        return f"Статус операции {choice_status} недоступен"

    list_operations_filter_status = []
    if choice_status == "executed":
        print("Операции отфильтрованы по статусу: 'EXECUTED'")
        list_operations_filter_status = filter_by_state(list_operations, 'EXECUTED')
    elif choice_status == "canceled":
        print("Операции отфильтрованы по статусу: 'CANCELED'")
        list_operations_filter_status = filter_by_state(list_operations, 'CANCELED')
    elif choice_status == "pending":
        print("Операции отфильтрованы по статусу: 'PENDING'")
        list_operations_filter_status = filter_by_state(list_operations, 'PENDING')
    else:
        print(f"Статус операции {choice_status} недоступен. Попытки исчерпаны. Программа завершена.")

    list_operations_filter_status_by_date = []
    print("Отсортировать операции по дате? Да/Нет")
    user_input = input("Введите Да или Нет: ").lower()
    if user_input == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input("Введите по возрастанию/по убыванию: ").lower()
        if user_input == "по возрастанию":
            list_operations_filter_status_by_date = sort_by_date(list_operations_filter_status, date=False)
        elif user_input == "по убыванию":
            list_operations_filter_status_by_date = sort_by_date(list_operations_filter_status)

    if list_operations_filter_status_by_date:
        list_operations_filter_status = list_operations_filter_status_by_date

    list_operations_filter_status_currency = []
    print("Выводить только рублевые транзакции? Да/Нет")
    user_input = input("Введите Да или Нет: ").lower()
    if user_input == "да":
        list_operations_filter_status_currency = filter_by_currency(list_operations_filter_status, "RUB")

    if list_operations_filter_status_currency:
        list_operations_filter_status = list_operations_filter_status_currency

    list_operations_filter_status_search = []
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input = input("Введите Да или Нет: ").lower()
    if user_input == "да":
        text = input("Введите поисковое слово: ")
        list_operations_filter_status_search = search_string_in_operations(list_operations_filter_status, text)
        if not list_operations_filter_status_search:
            return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"

    if user_input != "да":
        list_operations_filter_status = list_operations_filter_status

    if list_operations_filter_status_search:
        list_operations_filter_status = list_operations_filter_status_search
    print("Распечатываю итоговый список транзакций...")

    number_of_operations = len(list(list_operations_filter_status))
    if not number_of_operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    print(f"Всего банковских операций в выборке: {number_of_operations}")

    description = transaction_descriptions(list(list_operations_filter_status))

    for operations in list_operations_filter_status:
        date_operations = get_date(operations.get("date"))
        print(f"{date_operations} {next(description)}")
        from_number = mask_account_card(operations.get("from", ""))
        to_number = mask_account_card(operations.get("to"))
        print(f"{from_number} -> {to_number}")
        if operations.get("operationAmount"):
            amount = operations.get("operationAmount").get("amount")
            print(f"Сумма: {amount}")
    return ""


if __name__ == "__main__":
    print(main())
