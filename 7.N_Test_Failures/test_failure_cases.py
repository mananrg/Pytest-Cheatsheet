#test_failure_cases.py
def test_divide_by_zero():
    assert 1 / 0 == 2

def test_negative_number():
    assert abs(-5) == -5

def test_nonexistent_key():
    my_dict = {"key1": "value1", "key2": "value2"}
    assert my_dict["nonexistent_key"] == "value2"
