import pytest

from solution import Solution

soluton = Solution()

def test_numDistinct():
    assert soluton.numDistinct("rabbbit", "rabbit") == 3
    assert soluton.numDistinct("babgbag", "bag") == 5
    assert soluton.numDistinct("ABCDE", "AEC") == 0
    assert soluton.numDistinct("qqqqqq", "") == 1
    assert soluton.numDistinct("", "") == 1
    assert soluton.numDistinct("A", "A") == 1
    assert soluton.numDistinct("AB", "A") == 1
    assert soluton.numDistinct("AB", "B") == 1
    assert soluton.numDistinct("ABB", "AB") == 2
    assert soluton.numDistinct("ABABA", "ABA") == 3