import pytest


@pytest.fixture
def card() -> str:
    return "2456856384689354"


@pytest.fixture
def account() -> str:
    return "12345456367898765432"


@pytest.fixture
def date() -> str:
    return "2024-12-06T02:26:18.671407"
