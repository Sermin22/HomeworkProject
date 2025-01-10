from typing import Any, Callable
from time import time
from functools import wraps


def log(filename: Any = None) -> Callable:
    '''Декоратор логирующий начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
Принимает необязательный аргумент filename, который определяет, куда будут записываться логи
(в файл или в консоль). Если filename задан, логи записываются в указанный файл.
Если filename не задан, логи выводятся в консоль.'''

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable:
            log_message = ""
            start_time = time()
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
                result = None
            finally:
                end_time = time()
                print(f"Start time: {start_time}, End time: {end_time}")
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
            return result
        return wrapper
    return decorator


# if __name__ == "__main__":
#     # @log(filename="mylog.txt")
#     @log()
#     def my_function(x, y):
#         return x + y
#
#     my_function(1, "2")
