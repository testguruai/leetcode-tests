import pytest

from solution import Solution


class TestSolution:
    def test_compareVersion(self):
        solution = Solution()

        assert solution.compareVersion("1.0.1", "1") == 1
        assert solution.compareVersion("1.2", "1.10") == -1
        assert solution.compareVersion("2.4.3", "2.4.3") == 0
        assert solution.compareVersion("1.1.2", "1.01.2") == 0
        assert solution.compareVersion("1.0", "1.0.0") == 0
        
        with pytest.raises(TypeError):
            solution.compareVersion(1, 2)