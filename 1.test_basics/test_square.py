import math
import pytest
# Test 1
# Test square root of 25 equals 5
@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


# Test 2
# Test if 7 squared equals 49
@pytest.mark.square
def testsquare():
    num = 7
    assert 7 * 7 == 40


# Invalid test name, Hence wont execute in our test
@pytest.mark.others
def tesequality():
    assert 10 == 11


# To run pytest or pytest -v
