import pytest

class TestSolution:
    def test_firstMissingPositive(self):
        solution = Solution()
        assert solution.firstMissingPositive([1, 2, 0]) == 3
        assert solution.firstMissingPositive([3, 4, -1, 1]) == 2
        assert solution.firstMissingPositive([7, 8, 9, 11, 12]) == 1
        assert solution.firstMissingPositive([]) == 1
        assert solution.firstMissingPositive([-1, -2, -3]) == 1
        assert solution.firstMissingPositive([1, 1, 2, 2, 3, 3]) == 4

    def test_firstMissingPositive_invalid_input(self):
        solution = Solution()
        with pytest.raises(TypeError):
            solution.firstMissingPositive(None)
        with pytest.raises(TypeError):
            solution.firstMissingPositive(123)
        with pytest.raises(TypeError):
            solution.firstMissingPositive("123")
        with pytest.raises(ValueError):
            solution.firstMissingPositive([-1, -2, 0])
        with pytest.raises(ValueError):
            solution.firstMissingPositive([1, 2, 3.0])
        with pytest.raises(ValueError):
            solution.firstMissingPositive([1, 2, "3"])