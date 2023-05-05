import pytest
from solution import Solution

class TestSolution:
  def test_thirdMax(self):
    sol = Solution()

    nums1 = [3, 2, 1]
    assert sol.thirdMax(nums1) == 1

    nums2 = [1, 2]
    assert sol.thirdMax(nums2) == 2

    nums3 = [2, 2, 3, 1]
    assert sol.thirdMax(nums3) == 1

    nums4 = [5, 2, 2]
    assert sol.thirdMax(nums4) == 5

    nums5 = [1, 2, 2, 5, 3, 5]
    assert sol.thirdMax(nums5) == 2

    nums6 = [4, 5, 5, 6]
    assert sol.thirdMax(nums6) == 4

    nums7 = [4, 3, -1]
    assert sol.thirdMax(nums7) == 4

    nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sol.thirdMax(nums8) == 8

    nums9 = [1, 2, 2, 2, 3, 5]
    assert sol.thirdMax(nums9) == 2

    nums10 = []
    with pytest.raises(ValueError):
      sol.thirdMax(nums10)  # raises ValueError for empty list