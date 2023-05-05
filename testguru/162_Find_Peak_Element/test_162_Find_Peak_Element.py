import pytest

from solution import Solution

def test_findPeakElement():
    sol = Solution()
    
    assert sol.findPeakElement([1, 2, 3, 1]) == 2
    assert sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
    assert sol.findPeakElement([1, 2, 3, 4, 5, 6, 7]) == 6
    assert sol.findPeakElement([7, 6, 5, 4, 3, 2, 1]) == 0
    assert sol.findPeakElement([1]) == 0
    assert sol.findPeakElement([1, 2]) == 1
    assert sol.findPeakElement([2, 1]) == 0 
    
    assert sol.findPeakElement([]) == 0
    assert sol.findPeakElement(None) == 0
    assert sol.findPeakElement('not a list') == 0
    assert sol.findPeakElement(['not', 'a', 'list']) == 0