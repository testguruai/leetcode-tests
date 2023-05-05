import pytest
from solution import Solution

def test_numDecodings():
    sol = Solution()
    
    # Test case where s is an empty string
    assert sol.numDecodings("") == 0
    
    # Test case where s contains only 1 digit
    assert sol.numDecodings("0") == 0
    assert sol.numDecodings("3") == 1
    
    # Test case where s contains only 2 digits
    assert sol.numDecodings("00") == 0
    assert sol.numDecodings("01") == 0
    assert sol.numDecodings("27") == 1
    assert sol.numDecodings("12") == 2
    
    # Test case where s contains more than 2 digits
    assert sol.numDecodings("111") == 3
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("12893") == 2
    assert sol.numDecodings("10") == 1
    assert sol.numDecodings("301") == 0
