import pytest


class TestSolution:
    def test_moveZeroes1(self):
        sol = Solution()
        nums = [0, 1, 0, 3, 12]
        sol.moveZeroes(nums)
        assert nums == [1, 3, 12, 0, 0]

    def test_moveZeroes2(self):
        sol = Solution()
        nums = [0, 1, 0, 2, 0, 3, 0]
        sol.moveZeroes(nums)
        assert nums == [1, 2, 3, 0, 0, 0, 0]

    def test_moveZeroes3(self):
        sol = Solution()
        nums = [1, 2, 3]
        sol.moveZeroes(nums)
        assert nums == [1, 2, 3]

    def test_moveZeroes4(self):
        sol = Solution()
        nums = [0, 0, 0]
        sol.moveZeroes(nums)
        assert nums == [0, 0, 0]

    def test_moveZeroes5(self):
        sol = Solution()
        nums = []
        sol.moveZeroes(nums)
        assert nums == []