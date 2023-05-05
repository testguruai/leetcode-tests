import pytest

class TestSolution:

    def test_searchMatrix_with_empty_matrix(self):
        s = Solution()
        assert s.searchMatrix([], 5) == False

    def test_searchMatrix_with_invalid_matrix_values(self):
        s = Solution()
        assert s.searchMatrix(([[1, 2], [3, 4]]), 5) == False
        assert s.searchMatrix(([[1, 3], [5, 7]]), 9) == False

    def test_searchMatrix_with_matrix_values_in_range(self):
        s = Solution()
        assert s.searchMatrix(([[1, 3, 5], [7, 9, 11], [13, 15, 17]]), 1) == True
        assert s.searchMatrix(([[1, 3, 5], [7, 9, 11], [13, 15, 17]]), 7) == True
        assert s.searchMatrix(([[1, 3, 5], [7, 9, 11], [13, 15, 17]]), 15) == True

    def test_searchMatrix_with_matrix_values_out_of_range(self):
        s = Solution()
        assert s.searchMatrix(([[1, 3, 5], [7, 9, 11], [13, 15, 17]]), 0) == False
        assert s.searchMatrix(([[1, 3, 5], [7, 9, 11], [13, 15, 17]]), 18) == False

    def test_searchMatrix_with_same_values(self):
        s = Solution()
        assert s.searchMatrix(([[1, 1], [1, 1]]), 1) == True
        
    def test_searchMatrix_with_negative_values(self):
        s = Solution()
        assert s.searchMatrix(([[1, 3, 3], [7, -3, 2], [13, 16, 17]]), -3) == True
        assert s.searchMatrix(([[1, -3, 5], [-7, 9, 11], [-13, 15, 17]]), 2) == False