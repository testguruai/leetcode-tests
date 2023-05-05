import pytest

from typing import List

class Interval:
    def __init__(self, s: int = 0, e: int = 0):
        self.start = s
        self.end = e

@pytest.fixture
def interval_list():
    return [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]

def test_merge_invalid_input():
    s = Solution()
    assert s.merge(None) is None

def test_merge_one_element():
    s = Solution()
    intervals = [Interval(1,3)]
    assert s.merge(intervals) == intervals

def test_merge_two_non_overlapping_intervals():
    s = Solution()
    intervals = [Interval(1,3), Interval(4,6)]
    assert s.merge(intervals) == intervals

def test_merge_two_overlapping_intervals():
    s = Solution()
    intervals = [Interval(1,4), Interval(3,6)]
    assert s.merge(intervals) == [Interval(1,6)]

def test_merge_multiple_overlapping_intervals(interval_list):
    s = Solution()
    assert s.merge(interval_list) == [Interval(1,6), Interval(8,10), Interval(15,18)]