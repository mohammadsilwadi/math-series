from math_series import __version__
from math_series.math_series import fibonacci

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    # assign => what is the output that i resive
    actual = fibonacci(6)
    # arrange => what output do i expect to get
    expected = 8
    # assert => check if the output is as expected
    assert actual == expected