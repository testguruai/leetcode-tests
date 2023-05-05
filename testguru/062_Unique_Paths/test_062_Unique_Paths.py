import pytest

from solution import Solution

def test_uniquePaths():
    s = Solution()
    assert s.uniquePaths(3, 3) == 6
    assert s.uniquePaths(7, 3) == 28
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(1, 1) == 1
    assert s.uniquePaths(1, 10) == 1
    assert s.uniquePaths(5, 5) == 70
    assert s.uniquePaths(0, 0) == 0
    assert s.uniquePaths(0, 5) == 0
    assert s.uniquePaths(5, 0) == 0
    assert s.uniquePaths(23, 12) == 193536720

def test_uniquePaths_raises_TypeError():
    s = Solution()
    with pytest.raises(TypeError):
        s.uniquePaths('a', 3)
    with pytest.raises(TypeError):
        s.uniquePaths(3, 'b')
    with pytest.raises(TypeError):
        s.uniquePaths([], 5)
    with pytest.raises(TypeError):
        s.uniquePaths(5, {})

def test_uniquePaths_raises_ValueError():
    s = Solution()
    with pytest.raises(ValueError):
        s.uniquePaths(-1, 3)
    with pytest.raises(ValueError):
        s.uniquePaths(3, -1)
    with pytest.raises(ValueError):
        s.uniquePaths(-2, -5)