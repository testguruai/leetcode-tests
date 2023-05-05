import pytest

class TestSolution:
    def test_threeSumSmaller(self):
        sol = Solution()
        
        nums1 = [3, 1, 0, -2]
        target1 = 4
        assert sol.threeSumSmaller(nums1, target1) == 3
        
        nums2 = [-1, 0, 2, 5, 10]
        target2 = 5
        assert sol.threeSumSmaller(nums2, target2) == 2
        
        nums3 = [1, 1, 1, 1, 0]
        target3 = 3
        assert sol.threeSumSmaller(nums3, target3) == 7
        
        nums4 = [2, 2, 2]
        target4 = 2
        assert sol.threeSumSmaller(nums4, target4) == 0
        
    def test_twoSumSmaller(self):
        sol = Solution()
        
        nums1 = [3, 1, 0, -2]
        start1 = 1
        target1 = 4
        assert sol.twoSumSmaller(nums1, start1, target1) == 2
        
        nums2 = [-1, 0, 2, 5, 10]
        start2 = 1
        target2 = 5
        assert sol.twoSumSmaller(nums2, start2, target2) == 1
        
        nums3 = [1, 1, 1, 1, 0]
        start3 = 2
        target3 = 2
        assert sol.twoSumSmaller(nums3, start3, target3) == 2
        
        nums4 = [2, 2, 2]
        start4 = 1
        target4 = 2
        assert sol.twoSumSmaller(nums4, start4, target4) == 0        
    
    def test_binarySearch(self):
        sol = Solution()
        
        nums1 = [1, 3, 5, 6, 8]
        start1 = 0
        target1 = 4
        assert sol.binarySearch(nums1, start1, target1) == 1
        
        nums2 = [-2, -1, 0, 2, 5]
        start2 = 2
        target2 = 1
        assert sol.binarySearch(nums2, start2, target2) == 2
        
        nums3 = [1, 1, 3, 4]
        start3 = 0
        target3 = 2
        assert sol.binarySearch(nums3, start3, target3) == 1
        
        nums4 = [1, 2, 2, 3, 4]
        start4 = 0
        target4 = 2
        assert sol.binarySearch(nums4, start4, target4) == 1