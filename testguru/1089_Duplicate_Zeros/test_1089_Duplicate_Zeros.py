import pytest

from .solution import Solution

def test_duplicateZeros():
    s = Solution()
    # Example 1
    arr = [1,0,2,3,0,4,5,0]
    s.duplicateZeros(arr)
    assert arr == [1,0,0,2,3,0,0,4]

    # Example 2
    arr = [1,2,3]
    s.duplicateZeros(arr)
    assert arr == [1,2,3]

    # Only 0s
    arr = [0,0,0,0]
    s.duplicateZeros(arr)
    assert arr == [0,0,0,0]

    # Only 1s
    arr = [1,1,1,1]
    s.duplicateZeros(arr)
    assert arr == [1,1,1,1]

    # Single 0
    arr = [0]
    s.duplicateZeros(arr)
    assert arr == [0]

    # Single non-zero
    arr = [5]
    s.duplicateZeros(arr)
    assert arr == [5]