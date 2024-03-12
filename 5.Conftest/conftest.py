import pytest

@pytest.fixture
def greeting():
    return "Hello"

@pytest.fixture
def name():
    return "Alice"

@pytest.fixture
def age():
    return 30
