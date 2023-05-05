import pytest

from solution import Solution

class TestSolution:
    def test_containsDuplicate(self):
        s = Solution()

        # Test case 1 - valid input
        nums1 = [1, 2, 3, 4, 5]
        assert s.containsDuplicate(nums1) == False

        # Test case 2 - valid input
        nums2 = [1, 2, 3, 4, 5, 1]
        assert s.containsDuplicate(nums2) == True

        # Test case 3 - valid input
        nums3 = [1, 1, 1, 1, 1]
        assert s.containsDuplicate(nums3) == True

        # Test case 4 - edge case
        nums4 = []
        assert s.containsDuplicate(nums4) == False

        # Test case 5 - edge case
        nums5 = [1]
        assert s.containsDuplicate(nums5) == False

        # Test case 6 - edge case
        nums6 = [1, 1]
        assert s.containsDuplicate(nums6) == True