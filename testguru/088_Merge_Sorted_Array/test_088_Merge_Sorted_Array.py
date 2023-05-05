import pytest

@pytest.fixture
def solution():
  return Solution()

def test_merge(solution):
  # Test case where both arrays are empty
  nums1 = []
  m = 0
  nums2 = []
  n = 0
  solution.merge(nums1, m, nums2, n)
  assert nums1 == []

  # Test case where only nums1 is empty
  nums1 = []
  m = 0
  nums2 = [1,2,3,4]
  n = 4
  solution.merge(nums1, m, nums2, n)
  assert nums1 == [1,2,3,4]

  # Test case where only nums2 is empty
  nums1 = [1,2,3,4]
  m = 4
  nums2 = []
  n = 0
  solution.merge(nums1, m, nums2, n)
  assert nums1 == [1,2,3,4]

  # Test case where nums1 and nums2 have one element each
  nums1 = [2]
  m = 1
  nums2 = [1]
  n = 1
  solution.merge(nums1, m, nums2, n)
  assert nums1 == [1,2]

  # Test case where nums1 has more elements than nums2
  nums1 = [4,5,6,0,0,0]
  m = 3
  nums2 = [1,2,3]
  n = 3
  solution.merge(nums1, m, nums2, n)
  assert nums1 == [1,2,3,4,5,6]

  # Test case where nums2 has more elements than nums1
  nums1 = [0,0,0,1,2,3]
  m = 3
  nums2 = [4,5,6]
  n = 3
  solution.merge(nums1, m, nums2, n)
  assert nums1 == [0,1,2,3,4,5,6]