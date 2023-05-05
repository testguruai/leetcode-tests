import pytest

from solution import Solution

def test_findMin():
    sol = Solution()

    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([1]) == 1
    assert sol.findMin([1, 2]) == 1
    assert sol.findMin([2, 1]) == 1

    # Includes duplicates
    assert sol.findMin([1, 3, 3]) == 1
    assert sol.findMin([2, 2, 2, 0, 1]) == 0

    # Invalid inputs
    with pytest.raises(TypeError):
        sol.findMin(None)
    with pytest.raises(TypeError):
        sol.findMin("abc")
    with pytest.raises(ValueError):
        sol.findMin([])