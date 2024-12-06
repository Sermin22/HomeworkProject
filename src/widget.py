def mask_account_card(card_or_account_number: str) -> str:
    """
    Принимает на вход номер карты или счета и возвращает маску.
    Номер карты или счета замаскирован.
    """
    name_number = ""
    numbers = ""
    card_number = ""
    account_number = ""

    for number in card_or_account_number:
        if number.isalpha() or number == " ":
            name_number += number
        if number.isdigit():
            numbers += number

    if len(numbers) == 16:
        card_number +=numbers
    elif len(numbers) == 20:
        account_number += numbers
    else:
        return"Введен неправильный номер карты или счета"

    if card_number:
        return f"{name_number} {card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    elif account_number:
        return f"{name_number} **{account_number[16:]}"


def get_date(entrance_date: str) -> str:
    """Меняет формат даты"""

    date = entrance_date[8:10]
    month = entrance_date[5:7]
    year = entrance_date[0:4]
    return f"ДД.ММ.ГГГГ   ( {date}.{month}.{year} )"


if __name__ == "__main__":
    card_or_account = input("Укажите название карты или укажите, что это счет \
и далее введите номер ")
    print(mask_account_card(card_or_account))

    print(get_date("2024-12-06T02:26:18.671407"))
