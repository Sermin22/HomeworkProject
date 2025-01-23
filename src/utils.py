import os
from typing import Any
import json
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(BASE_DIR, 'logs', 'utils.log')

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_path, 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def list_financial_transactions(file_json: str) -> list[dict[Any, Any]]:
    '''Принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях'''
    try:
        with open(file_json, encoding="utf-8") as file:
            try:
                data = json.load(file)
                logger.info('Данные для обработки записаны в файл')
            except json.JSONDecodeError:
                logger.error('Недопустимые данные для выполнения успешной обработки')
                return []
    except FileNotFoundError:
        logger.error('Файл не найден или не существует для выполнения успешной обработки')
        return []
    if data and isinstance(data, list):
        logger.info('Получен список с данными о финансовых транзакциях')
        return data
    else:
        logger.error('Записанный файл не соответствует требованиям')
        return []


# if __name__ == "__main__":
#     print(list_financial_transactions("../data/transactions.json"))
