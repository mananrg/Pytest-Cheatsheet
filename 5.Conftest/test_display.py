def test_display_greeting(greeting, name):
    assert greeting + ", " + name == "Hello, Alice"

def test_display_age(greeting, age):
    assert greeting + ", " + str(age) == "Hello, 30"
 