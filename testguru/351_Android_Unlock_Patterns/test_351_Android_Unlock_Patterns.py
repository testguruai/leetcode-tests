import pytest
from solution import Solution

def test_numberOfPatterns():
    sol = Solution()
    assert sol.numberOfPatterns(1, 1) == 9
    assert sol.numberOfPatterns(1, 2) == 65
    assert sol.numberOfPatterns(1, 3) == 385
    assert sol.numberOfPatterns(2, 2) == 56
    assert sol.numberOfPatterns(2, 3) == 320
    assert sol.numberOfPatterns(3, 3) == 160

def test_is_valid():
    sol = Solution()
    used = [False] * 9

    # Test first digit is valid
    assert sol.is_valid(used, 0, -1) == True

    # Test using marked index is not valid
    used[1] = True
    assert sol.is_valid(used, 1, -1) == False

    # Test using adjacent cells (in a row or column) is valid
    used[1] = False
    assert sol.is_valid(used, 1, 0) == True
    assert sol.is_valid(used, 5, 4) == True

    # Test using adjacent cells on diagonal is valid
    assert sol.is_valid(used, 2, 0) == True
    assert sol.is_valid(used, 6, 4) == True

    # Test using other cells which are not adjacent is valid
    used[4] = True
    assert sol.is_valid(used, 0, 4) == True
    assert sol.is_valid(used, 7, 4) == True

def test_calc_patterns():
    sol = Solution()
    used = [False] * 9

    # Test length 0 returns 1
    assert sol.calc_patterns(used, -1, 0) == 1

    # Test number of patterns for length 1
    assert sol.calc_patterns(used, -1, 1) == 9

    # Test number of patterns for length 2
    assert sol.calc_patterns(used, -1, 2) == 56

    # Test number of patterns for length 3
    assert sol.calc_patterns(used, -1, 3) == 320