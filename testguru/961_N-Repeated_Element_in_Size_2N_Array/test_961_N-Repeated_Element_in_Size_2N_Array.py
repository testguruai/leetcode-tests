import collections
from typing import List
import pytest


class TestSolution:
    @pytest.fixture()
    def solution(self):
        return Solution()

    def test_repeatedNTimes(self, solution):
        assert solution.repeatedNTimes([1, 2, 3, 3]) == 3

    def test_repeatedNTimes_with_unexpected_data(self, solution):
        with pytest.raises(TypeError):
            solution.repeatedNTimes()

    def test_repeatedNTimes_with_no_common_elements(self, solution):
        assert solution.repeatedNTimes([1, 2, 3, 4]) == None

    def test_repeatedNTimes_with_multiple_common_elements(self, solution):
        assert solution.repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2

    def test_repeatedNTimes_with_all_common_elements(self, solution):
        assert solution.repeatedNTimes([5, 5, 5, 5, 5, 5, 5, 5]) == 5

    def test_repeatedNTimes_returns_int(self, solution):
        result = solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])
        assert isinstance(result, int)
        
    # testing the most common elements count
    def test_repeatedNTimes_returns_2nd_most_common_element(self, solution):
        assert solution.repeatedNTimes([5, 5, 5, 5, 2, 2, 3, 3]) == 2