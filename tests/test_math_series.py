from math_series import __version__
from math_series.math_series import fibonacci,lucas_numbers,sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    # assign : assign value inside the function
    actual = fibonacci(6)
    # arrange : what output do i expect to get
    expected = 8
    # assert : check if the output is as expected
    assert actual == expected
def test_tow():
    # assign : assign value inside the function
    actual = lucas_numbers(6)
    # arrange : what output do i expect to get
    expected = 18
    # assert : check if the output is as expected
    assert actual == expected
def test_three():
    # assign : assign value inside the function
    actual = sum_series(6)
    # arrange : what output do i expect to get
    expected = 8
    # assert : check if the output is as expected
    assert actual == expected
def test_four():
    # assign : assign value inside the function
    actual = sum_series(6,3,4)
    # arrange : what output do i expect to get
    expected = 18
    # assert : check if the output is as expected
    assert actual == expected
def test_five():
    # assign : assign value inside the function
    actual = sum_series(5)
    # arrange : what output do i expect to get
    expected = 5
    # assert : check if the output is as expected
    assert actual == expected
def test_six():
    # assign : assign value inside the function
    actual = sum_series(5,3,4)
    # arrange : what output do i expect to get
    expected = 11
    # assert : check if the output is as expected
    assert actual == expected