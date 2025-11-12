import pytest
from square import square

def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(5) == 25

def test_square_negative():
    assert square(-3) == 9
    assert square(-1) == 1
    assert square(-10) == 100

def test_square_large():
    assert square(1000) == 1000000
    assert square(12345) == 152399025

def test_square_float():
    assert square(2.5) == 6.25
    assert square(-3.1) == pytest.approx(9.61)
    assert square(0.0) == 0.0

def test_square_type_error():
    try:
        square("a string")
        assert False, "Expected TypeError"
    except TypeError:
        pass

    


