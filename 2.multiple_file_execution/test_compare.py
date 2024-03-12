import pytest
# Test 1
# Test if num is greater than 100
# @pytest.mark.xfail
# @pytest.mark.great
def test_greater():
    num = 100
    assert num > 100
# Test 2
# Test if num is greater than or equal to 100
# @pytest.mark.xfail
# @pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

# Test 3
# Test if num is less than 200
# @pytest.mark.skipif(True, reason="Test skipped because num is not less than 100")
# @pytest.mark.others
def test_less():
    num = 100
    assert num < 100


# To run pytest -v
