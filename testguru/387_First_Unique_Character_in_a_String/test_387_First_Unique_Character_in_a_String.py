import pytest
from solution import Solution

def test_firstUniqChar():
    sol = Solution()

    # Test case 1
    s = "leetcode"
    assert sol.firstUniqChar(s) == 0

    # Test case 2
    s = "loveleetcode"
    assert sol.firstUniqChar(s) == 2

    # Test case 3
    s = "aabbcc"
    assert sol.firstUniqChar(s) == -1

    # Test case 4
    s = ""
    assert sol.firstUniqChar(s) == -1

    # Test case 5
    s = "abababcdc"
    assert sol.firstUniqChar(s) == 8

    # Test case 6
    s = "hello world"
    assert sol.firstUniqChar(s) == 0

    # Test case 7
    s = "hheellllooo  wwoorrlldd"
    assert sol.firstUniqChar(s) == -1

    # Test case 8
    s = "abb"
    assert sol.firstUniqChar(s) == 1

    # Test case 9
    s = "a"
    assert sol.firstUniqChar(s) == 0

    # Test case 10
    s = "abcdefghijklmnopqrstuvwxyz"
    assert sol.firstUniqChar(s) == 0

    # Test case 11
    s = "aabb"
    assert sol.firstUniqChar(s) == -1

    # Test case 12
    s = "abba"
    assert sol.firstUniqChar(s) == 2

    # Test case 13
    s = "abacabadabacaba"
    assert sol.firstUniqChar(s) == 3

    # Test case 14
    s = "abacabadabacabae"
    assert sol.firstUniqChar(s) == 14

    # Test case 15
    s = "yyyyyyyyyyyyyyyzzzzzzzzzzzzz"
    assert sol.firstUniqChar(s) == -1