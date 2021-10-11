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