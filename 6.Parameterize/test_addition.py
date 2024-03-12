import pytest


@pytest.mark.parametrize(("x", "y", "result"), [(1, 1, 2), (2, 3, 5), (10, -5, 4)])
def test_add(x, y, result):
    assert x + y == result
