import pytest

# Mock function for isBadVersion API
def isBadVersion(version):
    if version >= 3:
        return True
    else:
        return False

# Test cases for Solution class
class TestSolution:
    def test_firstBadVersion(self):
        s = Solution()
        assert s.firstBadVersion(5) == 3
        assert s.firstBadVersion(10) == 3
        assert s.firstBadVersion(2) == 2
        assert s.firstBadVersion(1) == 1
        assert s.firstBadVersion(0) == 0
        
    def test_isBadVersion(self):
        assert isBadVersion(3) == True
        assert isBadVersion(5) == True
        assert isBadVersion(2) == False
        assert isBadVersion(0) == False