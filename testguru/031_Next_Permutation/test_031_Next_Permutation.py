import pytest

class TestSolution:
    def test_nextPermutation_example1(self):
        sol = Solution()
        nums = [1,2,3]
        sol.nextPermutation(nums)
        assert nums == [1,3,2]
    
    def test_nextPermutation_example2(self):
        sol = Solution()
        nums = [3,2,1]
        sol.nextPermutation(nums)
        assert nums == [1,2,3]
    
    def test_nextPermutation_example3(self):
        sol = Solution()
        nums = [1,1,5]
        sol.nextPermutation(nums)
        assert nums == [1,5,1]
    
    def test_nextPermutation_singleElement(self):
        sol = Solution()
        nums = [1]
        sol.nextPermutation(nums)
        assert nums == [1]
    
    def test_nextPermutation_emptyList(self):
        sol = Solution()
        nums = []
        sol.nextPermutation(nums)
        assert nums == []
    
    def test_swap_sameIndex(self):
        sol = Solution()
        nums = [1,2,3]
        sol.swap(nums, 1, 1)
        assert nums == [1,2,3]
    
    def test_swap_differentIndex(self):
        sol = Solution()
        nums = [1,2,3]
        sol.swap(nums, 0, 2)
        assert nums == [3,2,1]