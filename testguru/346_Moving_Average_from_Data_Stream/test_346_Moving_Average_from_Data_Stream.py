import pytest

@pytest.fixture
def moving_average():
    return MovingAverage(3)

def test_moving_average_initialization(moving_average):
    assert moving_average.size == 3
    assert moving_average.curr_range == []

def test_moving_average_next(moving_average):
    assert moving_average.next(1) == 1.0
    assert moving_average.curr_range == [1]
    assert moving_average.next(2) == 1.5
    assert moving_average.curr_range == [1, 2]
    assert moving_average.next(3) == 2.0
    assert moving_average.curr_range == [1, 2, 3]
    assert moving_average.next(4) == 3.0
    assert moving_average.curr_range == [2, 3, 4]
    assert moving_average.next(5) == 4.0
    assert moving_average.curr_range == [3, 4, 5]