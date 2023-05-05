import pytest

def test_fib():
    sol = Solution()
    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(3) == 2
    assert sol.fib(4) == 3
    assert sol.fib(5) == 5
    
def test_fib_raises_exception():
    sol = Solution()
    with pytest.raises(TypeError):
        sol.fib('a')
    with pytest.raises(TypeError):
        sol.fib([1,2])