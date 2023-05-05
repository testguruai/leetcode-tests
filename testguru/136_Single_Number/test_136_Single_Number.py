import pytest

class TestSolution:
    def test_singleNumber_with_hash(self):
        nums = [1, 2, 3, 2, 1]
        assert Solution().singleNumber(nums) == 3

    def test_singleNumber_with_set(self):
        nums = [1, 2, 3, 2, 1]
        assert Solution().singleNumber(nums) == 3

    def test_singleNumber_with_xor(self):
        nums = [1, 2, 3, 2, 1]
        assert Solution().singleNumber(nums) == 3

    def test_singleNumber_with_empty(self):
        nums = []
        assert Solution().singleNumber(nums) is None

    def test_singleNumber_with_one_element(self):
        nums = [1]
        assert Solution().singleNumber(nums) == 1