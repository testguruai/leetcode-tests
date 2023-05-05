import pytest

# test cases for majorityElement function

def test_majorityElement():
  # Test case for O(1) space
  s = Solution()
  assert s.majorityElement([1,2,3,1,2,3,1,2,3]) == [1, 2, 3]
  assert s.majorityElement([3,7,2,1,3,2,1,8,3,7,1]) == [1, 3]
  
  # Test case using dict
  assert s.majorityElement([1,2,3,1,2,3,1,2,3]) == [1, 2, 3]
  assert s.majorityElement([3,7,2,1,3,2,1,8,3,7,1]) == [1, 3]

  # Test case using a different method
  assert s.majorityElement([1,2,3,1,2,3,1,2,3]) == [1, 2, 3]
  assert s.majorityElement([3,7,2,1,3,2,1,8,3,7,1]) == [1, 3]