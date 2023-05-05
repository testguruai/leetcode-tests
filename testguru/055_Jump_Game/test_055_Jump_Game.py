import pytest

def test_canJump():
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False
    assert s.canJump([1, 1, 1, 0]) == True
    assert s.canJump([0]) == True
    assert s.canJump([0, 1]) == False
    assert s.canJump([2, 0, 0]) == True
    assert s.canJump([1, 0, 2]) == False

# Run the test.
test_canJump()