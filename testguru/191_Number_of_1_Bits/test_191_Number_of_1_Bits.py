import pytest

from solution import Solution

def test_hammingWeight():
    s = Solution()
    n1 = int('00000000000000000000000000001011', 2)
    assert s.hammingWeight(n1) == 3
    
    n2 = int('00000000000000000000000010000000', 2)
    assert s.hammingWeight(n2) == 1
    
    n3 = int('11111111111111111111111111111101', 2)
    assert s.hammingWeight(n3) == 31
    
    n4 = int('00000000000000000000000000000000', 2)
    assert s.hammingWeight(n4) == 0
    
    n5 = int('11111111111111111111111111111111', 2)
    assert s.hammingWeight(n5) == 32