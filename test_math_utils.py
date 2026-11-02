import pytest

from math_utils import add, average


def test_add_two_integers():
    assert add(2, 3) == 5


def test_add_negative_and_float():
    assert add(-1.5, 0.5) == -1.0


def test_average_of_numbers():
    assert average([1, 2, 3, 4]) == 2.5


def test_average_of_single_value():
    assert average([10]) == 10


def test_average_of_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        average([])
