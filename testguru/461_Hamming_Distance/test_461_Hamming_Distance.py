import pytest
from solution import Solution

class TestSolution:
    def test_hammingDistance_equal_numbers(self):
        sol = Solution()
        assert sol.hammingDistance(5, 5) == 0

    def test_hammingDistance_different_numbers(self):
        sol = Solution()
        assert sol.hammingDistance(1, 4) == 2

    def test_hammingDistance_large_numbers(self):
        sol = Solution()
        assert sol.hammingDistance(123456, 654321) == 15

    def test_hammingDistance_zero_numbers(self):
        sol = Solution()
        assert sol.hammingDistance(0, 0) == 0

    def test_hammingDistance_negative_numbers(self):
        sol = Solution()
        assert sol.hammingDistance(-1, -4) == 1

    def test_hammingDistance_one_negative_number(self):
        sol = Solution()
        assert sol.hammingDistance(-1, 4) == 1

    def test_hammingDistance_max_integers(self):
        sol = Solution()
        assert sol.hammingDistance(2147483647, 0) == 31

    def test_hammingDistance_min_integers(self):
        sol = Solution()
        assert sol.hammingDistance(-2147483648, 0) == 1

    def test_hammingDistance_large_integers(self):
        sol = Solution()
        assert sol.hammingDistance(1234567890, 987654321) == 18

    def test_hammingDistance_mixed_integers(self):
        sol = Solution()
        assert sol.hammingDistance(1234567890, -987654321) == 19

    def test_hammingDistance_string_numbers(self):
        sol = Solution()
        with pytest.raises(TypeError):
            sol.hammingDistance('123', '456')