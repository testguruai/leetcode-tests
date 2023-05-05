# Import pytest library
import pytest

# Import the class Solution
from solution import Solution

# Create a test class for the Solution class
class TestSolution:
  
    # Create a test method to test the function findLengthOfLCIS with an empty list of integers
    def test_findLengthOfLCIS_empty_list(self):
        assert Solution().findLengthOfLCIS([]) == 0

    # Create a test method to test the function findLengthOfLCIS with a list of integers in ascending order
    def test_findLengthOfLCIS_sorted_list(self):
        assert Solution().findLengthOfLCIS([1, 2, 3, 4, 5]) == 5

    # Create a test method to test the function findLengthOfLCIS with a list of integers in descending order
    def test_findLengthOfLCIS_reverse_sorted_list(self):
        assert Solution().findLengthOfLCIS([5, 4, 3, 2, 1]) == 1

    # Create a test method to test the function findLengthOfLCIS with a list of integers with repeated values
    def test_findLengthOfLCIS_list_with_repeated_values(self):
        assert Solution().findLengthOfLCIS([1, 2, 2, 3, 4, 4, 5, 5]) == 3

    # Create a test method to test the function findLengthOfLCIS with a list of integers with alternating values
    def test_findLengthOfLCIS_list_with_alternating_values(self):
        assert Solution().findLengthOfLCIS([1, 3, 2, 4, 3, 5]) == 3


# Run the tests
if __name__ == "__main__":
    pytest.main()