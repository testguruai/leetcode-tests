import pytest

from solution import Solution

def test_case_1():
    s = Solution()
    houses = [1, 2, 3]
    heaters = [2]
    assert s.findRadius(houses, heaters) == 1

def test_case_2():
    s = Solution()
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    assert s.findRadius(houses, heaters) == 1

def test_case_3():
    s = Solution()
    houses = [1, 2, 3, 5, 6]
    heaters = [1, 5]
    assert s.findRadius(houses, heaters) == 1

def test_case_4():
    s = Solution()
    houses = [1, 2, 3, 4, 5, 6]
    heaters = [1, 6]
    assert s.findRadius(houses, heaters) == 3

def test_case_5():
    s = Solution()
    houses = [1, 2, 3, 4, 5, 6]
    heaters = [7]
    assert s.findRadius(houses, heaters) == 6

def test_case_6():
    s = Solution()
    houses = [1, 2, 3, 4, 5, 6]
    heaters = [1]
    assert s.findRadius(houses, heaters) == 5

def test_case_7():
    s = Solution()
    houses = [1, 2, 3, 4, 5, 6]
    heaters = [2, 5]
    assert s.findRadius(houses, heaters) == 1

def test_case_8():
    s = Solution()
    houses = [1]
    heaters = [1]
    assert s.findRadius(houses, heaters) == 0

def test_case_9():
    s = Solution()
    houses = [1, 2, 3, 4, 5, 6]
    heaters = []
    assert s.findRadius(houses, heaters) == 0

def test_case_10():
    s = Solution()
    houses = []
    heaters = []
    assert s.findRadius(houses, heaters) == 0