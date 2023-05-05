import pytest

class TestWiggleSort:
    def test_wiggle_sort_empty_list(self):
        s = Solution()
        nums = []
        s.wiggleSort(nums)
        assert nums == []

    def test_wiggle_sort_one_element_list(self):
        s = Solution()
        nums = [1]
        s.wiggleSort(nums)
        assert nums == [1]

    def test_wiggle_sort_sorted_list(self):
        s = Solution()
        nums = [1, 2, 3, 4, 5]
        s.wiggleSort(nums)
        assert nums == [1, 3, 2, 5, 4]

    def test_wiggle_sort_reversed_list(self):
        s = Solution()
        nums = [5, 4, 3, 2, 1]
        s.wiggleSort(nums)
        assert nums == [4, 5, 2, 3, 1]

    def test_wiggle_sort_random_list(self):
        s = Solution()
        nums = [4, 3, 6, 1, 5, 2]
        s.wiggleSort(nums)
        assert nums == [3, 6, 1, 5, 2, 4]