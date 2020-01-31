import pytest

from numbers_to_dec import list_to_decimal


def test_not_int():
    with pytest.raises(TypeError):
        list_to_decimal([True])
        list_to_decimal([False])
        list_to_decimal()


def test_negative():
    with pytest.raises(ValueError):
        list_to_decimal([-1])
        list_to_decimal([10])
        list_to_decimal([])


def test_normal():
    assert list_to_decimal([9]) == 9
    assert list_to_decimal([0]) == 0
    assert list_to_decimal([0, 1, 2]) == 12
    assert list_to_decimal([1, 0, 1]) == 101
