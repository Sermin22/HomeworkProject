import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(BASE_DIR, 'logs', 'masks.log')

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_path, 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован.
    """

    # Вызывает исключение, если неверный тип данных
    if not isinstance(card_number, str):
        logger.error('Ошибка типа данных')
        raise TypeError('Ошибка типа данных')

    if card_number.isdigit() and len(card_number) == 16:
        logger.info('Номер карты успешно замаскирован')
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.error('Введен неправильный номер карты')
        return 'Введен неправильный номер карты'


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован.
    """

    # Вызывает на исключение, если неверный тип данных
    if not isinstance(account_number, str):
        logger.error('Ошибка типа данных')
        raise TypeError('Ошибка типа данных')

    if account_number.isdigit() and len(account_number) == 20:
        logger.info('Номер счета успешно замаскирован')
        return f"**{account_number[16:]}"
    else:
        logger.error('Введен неправильный номер счета')
        return "Введен неправильный номер счета"


if __name__ == "__main__":
    card_number: str = input("Введите номер карты: ")
    print(get_mask_card_number(card_number))

    account_number: str = input("Введите номер счета: ")
    print(get_mask_account(account_number))
