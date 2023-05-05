import pytest

from solution import Solution

def test_getModifiedArray():
    s = Solution()
    # Testcase 1
    length = 5
    updates = [[1,3,2],[2,4,3],[0,2,-2]]
    assert s.getModifiedArray(length, updates) == [-2,0,3,5,3]

    # Testcase 2
    length = 2
    updates = [[0,1,2]]
    assert s.getModifiedArray(length, updates) == [2,2]

    # Testcase 3
    length = 3
    updates = [[0,0,1],[1,1,1]]
    assert s.getModifiedArray(length, updates) == [1,2,1]

    # Testcase 4
    length = 4
    updates = [[0, 1, 2], [2, 3, 2]]
    assert s.getModifiedArray(length, updates) == [2, 4, 4, 2]