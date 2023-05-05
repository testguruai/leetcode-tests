import pytest

from solution import Solution

def test_reverse():
    sol = Solution()

    # Test case where the reversed integer is within the signed 32-bit integer limit.
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321

    # Test case where the reversed integer exceeds the signed 32-bit integer limit.
    assert sol.reverse(2147483647) == 0
    assert sol.reverse(-2147483648) == 0

    # Test case where the input integer is 0.
    assert sol.reverse(0) == 0