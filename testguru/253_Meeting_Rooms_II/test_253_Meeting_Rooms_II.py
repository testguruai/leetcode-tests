import pytest
from solution import Interval, Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.fixture
def intervals():
    return [Interval(1, 3), Interval(2, 4), Interval(5, 7), Interval(6, 8)]

def test_minMeetingRooms_returns_correct_number_of_rooms(solution, intervals):
    assert solution.minMeetingRooms(intervals) == 2

def test_minMeetingRooms_returns_zero_for_empty_input(solution):
    assert solution.minMeetingRooms([]) == 0

def test_minMeetingRooms_returns_one_for_single_interval(solution):
    assert solution.minMeetingRooms([Interval(2, 4)]) == 1

def test_minMeetingRooms_returns_correct_number_of_rooms_for_overlapping_intervals(solution):
    intervals = [Interval(1, 3), Interval(2, 4), Interval(3, 5), Interval(4, 6)]
    assert solution.minMeetingRooms(intervals) == 3

def test_minMeetingRooms_returns_correct_number_of_rooms_for_non_overlapping_intervals(solution):
    intervals = [Interval(1, 3), Interval(4, 6), Interval(7, 9)]
    assert solution.minMeetingRooms(intervals) == 1