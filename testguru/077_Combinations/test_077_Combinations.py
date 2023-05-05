import pytest

def test_get_combine():
    s = Solution()
    res = []
    s.get_combine(res, [], 4, 2, 1)
    assert res == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

def test_combine():
    s = Solution()
    assert s.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combine(3, 2) == [[1, 2], [1, 3], [2, 3]]
    assert s.combine(5, 3) == [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    assert s.combine(1, 1) == [[1]]
    assert s.combine(0, 0) == [[]]