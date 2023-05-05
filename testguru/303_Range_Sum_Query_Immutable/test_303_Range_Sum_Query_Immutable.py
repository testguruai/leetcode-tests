import pytest


@pytest.fixture
def num_array():
    return NumArray([1, 2, 3, 4, 5])


def test_sumRange(num_array):
    assert num_array.sumRange(0, 0) == 1
    assert num_array.sumRange(0, 1) == 3
    assert num_array.sumRange(1, 3) == 9
    assert num_array.sumRange(2, 4) == 12
    assert num_array.sumRange(0, 4) == 15

def test_empty_array():
    num_array = NumArray([])
    assert num_array.sumRange(0,0) == 0


def test_negative_values(num_array):
    assert num_array.sumRange(-1, 3) == 6
    assert num_array.sumRange(-2, -1) == 0