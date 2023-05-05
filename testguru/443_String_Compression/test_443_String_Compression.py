import pytest
from solution import Solution

def test_compress():
    solution = Solution()
    assert solution.compress(["a","a","b","b","c","c","c"]) == 6
    assert solution.compress(["a"]) == 1
    assert solution.compress(["a","b","b","c","c","c"]) == 5
    assert solution.compress([]) == 0
    assert solution.compress(["a", "a", "a", "a", "a"]) == 2
    assert solution.compress(["a", "b", "c"]) == 3
    assert solution.compress(["a", "a", "b", "b", "a", "a"]) == 6
    assert solution.compress(["a","a","b","b","c","c","c", "c"]) == 8
    assert solution.compress(["a","a","b","b","c","c","c", "c", "c"]) == 9
    assert solution.compress(["a","a","b","b","b","b","c","c","c"]) == 6
    
def test_compress_failure():
    solution = Solution()
    assert solution.compress(["a","a","b","b","c","c","c"]) != 7
    assert solution.compress(["a"]) != 2
    assert solution.compress(["a","b","b","c","c","c"]) != 6
    assert solution.compress(["a", "a", "a", "a", "a"]) != 5
    assert solution.compress(["a", "b", "c"]) != 2
    assert solution.compress(["a", "a", "b", "b", "a", "a"]) != 7
    assert solution.compress(["a","a","b","b","c","c","c", "c"]) != 12
    assert solution.compress(["a","a","b","b","c","c","c", "c", "c"]) != 10
    assert solution.compress(["a","a","b","b","b","b","c","c","c"]) != 5