
import pytest

def test_isPowerOfThree_true():
    assert Solution().isPowerOfThree(3) == True
    assert Solution().isPowerOfThree(27) == True
    
def test_isPowerOfThree_false():
    assert Solution().isPowerOfThree(0) == False
    assert Solution().isPowerOfThree(-3) == False
    assert Solution().isPowerOfThree(1) == False
    assert Solution().isPowerOfThree(2) == False
    assert Solution().isPowerOfThree(28) == False
