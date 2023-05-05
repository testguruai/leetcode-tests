import pytest
from solution import Solution

def test_min_distance():
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "") == 0
    assert s.minDistance("abc", "def") == 3
    assert s.minDistance("abcd", "dcba") == 4

def test_min_distance_with_whitespace():
    s = Solution()
    assert s.minDistance(" hello ", " world ") == 8
    assert s.minDistance(" hello world", "goodbye world        ") == 9
    assert s.minDistance("", "  ") == 2
    assert s.minDistance(" ", "") == 1

def test_min_distance_with_unicode():
    s = Solution()
    assert s.minDistance("zażółć", "gęślą jaźń") == 10
    assert s.minDistance("לילה", "ללאה") == 2
    assert s.minDistance("こんにちは", "さようなら") == 8
    assert s.minDistance("犬", "猫") == 1

def test_min_distance_with_numbers():
    s = Solution()
    assert s.minDistance("123456789", "987654321") == 8
    assert s.minDistance("12345", "12345789654") == 9
    assert s.minDistance("abc123", "def456gh") == 6

def test_min_distance_with_invalid_input():
    s = Solution()
    with pytest.raises(TypeError):
        s.minDistance(None, "hello")
    with pytest.raises(TypeError):
        s.minDistance("hello", None)
    with pytest.raises(TypeError):
        s.minDistance(None, None)
    with pytest.raises(TypeError):
        s.minDistance("hello", 123)
    with pytest.raises(TypeError):
        s.minDistance(456, "world")