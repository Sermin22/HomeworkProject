from src.masks import get_mask_card_number, get_mask_account

card_number: str = input("Введите номер карты: ")
print(get_mask_card_number(card_number))

account_number: str = input("Введите номер счета: ")
print(get_mask_account(account_number))
