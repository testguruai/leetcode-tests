import pytest

from solution import Solution

class Tests:
    def test_minimumTotal_returns_0_if_triangle_is_None_or_empty(self):
        solution = Solution()
        assert solution.minimumTotal(None) == 0
        assert solution.minimumTotal([]) == 0
        
    def test_minimumTotal_returns_minimum_sum_of_triangle(self):
        solution = Solution()
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
        assert solution.minimumTotal(triangle) == 11
        
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3],
            [9, 10, 11, 12, 13]
        ]
        assert solution.minimumTotal(triangle) == 21
        
        triangle = [
            [7]
        ]
        assert solution.minimumTotal(triangle) == 7
        
        triangle = [
            [7],
            [3, 8]
        ]
        assert solution.minimumTotal(triangle) == 10
        
        triangle = [
            [1],
            [2, 3],
            [4, 5, 6]
        ]
        assert solution.minimumTotal(triangle) == 6
        
        triangle = [
            [10]
        ]
        assert solution.minimumTotal(triangle) == 10
        
        triangle = [
            [1],
            [1, 1]
        ]
        assert solution.minimumTotal(triangle) == 2