import pytest
from mython.fizzbuzz import fizzbuzz

@pytest.mark.parametrize(('number', 'expected'), [
    (1, "1"),
    (2, "2"),
    (3, "fizz"),
    (4, "4"),
    (5, "buzz"),
    (6, "fizz"),
    (10, "buzz"),
    (11, "11"),
    (12, "fizz"),
    (15, "fizzbuzz"),
])

def test_fizzbuzz(number, expected):
    assert fizzbuzz(number) == expected
