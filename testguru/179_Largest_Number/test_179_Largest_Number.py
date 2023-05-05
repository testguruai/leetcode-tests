import pytest
from solution import Solution

def test_largestNumber():
    s = Solution()

    assert s.largestNumber([10, 2]) == '210'
    assert s.largestNumber([3, 30, 34, 5, 9]) == '9534330'
    assert s.largestNumber([0, 0]) == '0'
    assert s.largestNumber([1]) == '1'
    assert s.largestNumber([10, 10]) == '1010'