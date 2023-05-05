
import pytest

from solution import Solution

def test_findMaxConsecutiveOnes():
    solution = Solution()

    assert solution.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    assert solution.findMaxConsecutiveOnes([0,0,0,0,0]) == 0
    assert solution.findMaxConsecutiveOnes([1,1,1,1,1,1]) == 6
    assert solution.findMaxConsecutiveOnes([]) == 0
    assert solution.findMaxConsecutiveOnes([1,0,1,0,1]) == 1

def test_findMaxConsecutiveOnes_edge_cases():
    solution = Solution()

    assert solution.findMaxConsecutiveOnes([1]) == 1
    assert solution.findMaxConsecutiveOnes([0]) == 0
    assert solution.findMaxConsecutiveOnes([1,0,1,0,0,1,1]) == 2
    assert solution.findMaxConsecutiveOnes([1]*100000) == 100000

