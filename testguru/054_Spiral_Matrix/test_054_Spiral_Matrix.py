import pytest

from solution import Solution


def test_spiralOrder_empty():
    s = Solution()
    assert s.spiralOrder(None) == None
    assert s.spiralOrder([]) == []


def test_spiralOrder():
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1]]) == [1]
    assert s.spiralOrder([[1, 2, 3]]) == [1, 2, 3]
    assert s.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert s.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert s.spiralOrder([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [
        1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


def test_get_spiralOrder():
    s = Solution()
    assert s.get_spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 2, 0, 2) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.get_spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1, 1, 1) == [5]
    assert s.get_spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 1, 0, 1) == [1, 2, 4, 5]


if __name__ == '__main__':
    pytest.main()