import pytest
from solution import Solution

def test_countPrimes():
    sol = Solution()

    assert sol.countPrimes(10) == 4
    assert sol.countPrimes(5) == 2
    assert sol.countPrimes(25) == 9
    assert sol.countPrimes(0) == 0

    with pytest.raises(TypeError):
        sol.countPrimes("a")
        sol.countPrimes(None) 

    with pytest.raises(ValueError):
        sol.countPrimes(-1)	
        sol.countPrimes(-10)