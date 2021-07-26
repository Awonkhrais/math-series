from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'

# fibonacci tests : 

# fibonacci series : 0,1,1,2,3,5,8,13,....

def test_zero():

    expected = 0

    actual = fibonacci(0)

    assert expected == actual

def test_one():

    expected = 1

    actual = fibonacci(1)

    assert expected == actual


def test_six():

    expected = 8

    actual = fibonacci(6)

    assert expected == actual

# lucus tests : 

# lucas series : 2,1,3,4,7,11,....

def test_zero():
    expected = 2

    actual = lucas(0)

    assert expected == actual

def test_four():
    expected = 7

    actual = lucas(4)

    assert expected == actual


# sum series tests:(this one for Fibonacci )

def test_three():

    expected = 2

    actual = sum_series(3)

    assert expected == actual


