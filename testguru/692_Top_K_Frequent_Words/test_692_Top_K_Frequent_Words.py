
import pytest
from solution import Solution

def test_topKFrequent_1():
    s = Solution()
    assert s.topKFrequent(["hello", "world", "hello", "world", "and", "hello"], 2) == ["hello", "world"]

def test_topKFrequent_2():
    s = Solution()
    assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3) == ["i", "love", "coding"]

def test_topKFrequent_3():
    s = Solution()
    assert s.topKFrequent([], 1) == []

def test_topKFrequent_4():
    s = Solution()
    assert s.topKFrequent(["a", "a", "a", "b", "b", "c"], 2) == ["a", "b"]

def test_topKFrequent_5():
    s = Solution()
    assert s.topKFrequent(["this", "is", "a", "test"], 1) == ["a"]

if __name__ == '__main__':
    pytest.main()
