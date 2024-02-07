def test_add_integer():
    assert add_integer(2, 2) == 4
    assert add_integer(-5, 5) == 0
    assert add_integer(10.5, 5) == 15
    assert add_integer(10, -5) == 5
    assert add_integer(2.5, 2.5) == 5
    assert add_integer(0, 0) == 0


try:
    test_add_integer()
    print("All tests passed!")
except AssertionError as e:
    print("Test failed:", str(e))
