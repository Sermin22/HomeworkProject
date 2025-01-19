import pytest
from src.decorators import log


@log()
def my_function(x: int, y: int) -> int:
    return x + y


def test_successful_execution(capsys: pytest.CaptureFixture[str]) -> None:
    '''Тест успешного выполнения функции, обернутой декоратором log'''

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_error_handling(capsys: pytest.CaptureFixture[str]) -> None:
    '''Тест обработки ошибки декоратором, если в функцию передано не число'''

    my_function(1, "2")
    captured = capsys.readouterr()
    assert "my_function error:" in captured.out


def test_log_time(capsys: pytest.CaptureFixture[str]) -> None:
    '''Тест, что декоратор автоматически логирует начало и конец выполнения функции'''

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "Start time:" and "End time:" in captured.out
