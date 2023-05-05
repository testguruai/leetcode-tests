import pytest
class TestSolution:

  def test_maxSubArray(self):
    sol = Solution()
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([-1]) == -1
    assert sol.maxSubArray([-2,-1]) == -1
    assert sol.maxSubArray([-1,-2]) == -1
    assert sol.maxSubArray([5,4,-1,7,8]) == 23
    assert sol.maxSubArray([-5,-7,-9,-12]) == -5
    assert sol.maxSubArray([0,-1,0,5]) == 5
    assert sol.maxSubArray([-2,3,5]) == 8   


if __name__ == '__main__':
  pytest.main(argv=['first-arg-is-ignored'], exitcode=0)