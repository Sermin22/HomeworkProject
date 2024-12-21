from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """
    Принимает на вход номер карты или счета и возвращает маску.
    Номер карты или счета замаскирован.
    """
    # Вызывает исключение, если неверный тип данных
    if not isinstance(card_or_account_number, str):
        raise TypeError('Ошибка типа данных')

    name_number = ""
    numbers = ""
    card_number = ""
    account_number = ""
    for number in card_or_account_number:
        if number.isalpha():
            name_number += number
        if number.isdigit():
            numbers += number

    if len(numbers) == 16:
        card_number = get_mask_card_number(numbers)
    elif len(numbers) == 20:
        account_number = get_mask_account(numbers)
    else:
        return f"{name_number} введен некорректный номер карты или счета"

    if card_number:
        return f"{name_number} {card_number}"
    elif account_number:
        return f"{name_number} {account_number}"
    return ""


def get_date(entrance_date: str) -> str:
    """Меняет формат даты"""

    slice_date = entrance_date[:10].split("-")
    exit_date = ".".join(slice_date[::-1])
    return f"ДД.ММ.ГГГГ ( {exit_date} )"


if __name__ == "__main__":
    card_or_account = input(
        "Укажите название карты или укажите, что это счет \
и далее введите номер "
    )
    print(mask_account_card(card_or_account))

    print(get_date("2024-12-06T02:26:18.671407"))
