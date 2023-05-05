# Creating a test class for Solution module
class TestSolution:
    
    def test_findKthNumber(self):
        # Test Case 1
        m, n, k = 3, 3, 5
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 3
        
        # Test Case 2
        m, n, k = 3, 3, 7
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 4
        
        # Test Case 3
        m, n, k = 2, 3, 6
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 6
        
        # Test Case 4
        m, n, k = 5, 10, 50
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 59
        
        # Test Case 5
        m, n, k = 5, 12, 70
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 96
        
        # Test Case 6
        m, n, k = 10, 10, 100
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 116
        
        # Test Case 7
        m, n, k = 1, 1, 1
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == 1
        
        # Test Case 8 - Negative Test Case
        m, n, k = 5, 5, 60
        solution = Solution()
        assert solution.findKthNumber(m, n, k) != 31