import pytest

class TestSolution:
    def test_generateMatrix(self):
        s = Solution()

        # Test with n = 1
        assert s.generateMatrix(1) == [[1]]

        # Test with n = 2
        assert s.generateMatrix(2) == [[1, 2], [4, 3]]

        # Test with n = 3
        assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]] 

        # Test with n = 4
        assert s.generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]] 

        # Test with n = 5
        assert s.generateMatrix(5) == [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]