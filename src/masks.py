from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован.
    """

    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Введен неправильный номер карты"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован.
    """

    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[16:]}"
    else:
        return "Введен неправильный номер счета"


if __name__ == "__main__":
    card_number: str = input("Введите номер карты: ")
    print(get_mask_card_number(card_number))

    account_number: str = input("Введите номер счета: ")
    print(get_mask_account(account_number))
