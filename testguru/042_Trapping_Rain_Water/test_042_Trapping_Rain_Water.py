import pytest

from solution import Solution

def test_trap():
    s = Solution()
    assert s.trap([2,6,3,8,2,7,2,5,0]) == 11
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([]) == 0
    assert s.trap([1,2,3,4,5]) == 0
    assert s.trap([5,4,3,2,1]) == 0
    assert s.trap([1,1,1,1,1]) == 0
    assert s.trap([5,2,1,2,1,5]) == 14
    
def test_rain_water():
    s = Solution()
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 0, 3) == 3
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 3, 5) == 3
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 5, 7) == 3
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 7, 8) == 3
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 2, 3) == 0
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 4, 5) == 0
    assert s.rain_water([2,6,3,8,2,7,2,5,0], 0, 8) == 11