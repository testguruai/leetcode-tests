import pytest

from solution import Solution

def test_intToRoman():
    s = Solution()
    
    #Test Case 1
    result = s.intToRoman(90)
    assert result == 'XC'

    #Test Case 2
    result = s.intToRoman(150)
    assert result == 'CL'

    #Test Case 3
    result = s.intToRoman(3999)
    assert result == 'MMMCMXCIX'
    
    #Test Case 4
    result = s.intToRoman(0)
    assert result == ''