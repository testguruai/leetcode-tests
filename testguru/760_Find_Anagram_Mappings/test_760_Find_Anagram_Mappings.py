
import pytest

class TestSolution:
    def test_anagramMappings(self):
        sol = Solution()

        # Test Case 1
        A = [1, 2, 3, 4]
        B = [4, 3, 2, 1]
        expected_output = [3, 2, 1, 0]
        assert sol.anagramMappings(A, B) == expected_output

        # Test Case 2
        A = [1, 2, 3, 4]
        B = [4, 3, 2, 5]
        expected_output = [3, 2, 1, None]
        assert sol.anagramMappings(A, B) == expected_output

        # Test Case 3
        A = [1]
        B = [1]
        expected_output = [0]
        assert sol.anagramMappings(A, B) == expected_output

        # Test Case 4
        A = []
        B = []
        expected_output = []
        assert sol.anagramMappings(A, B) == expected_output

        # Test Case 5
        A = [1, 2, 3]
        B = [1, 2, 3]
        expected_output = [0, 1, 2]
        assert sol.anagramMappings(A, B) == expected_output
