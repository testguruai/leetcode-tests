import pytest
from solution import Solution

def test_isPalindrome_true():
    s = Solution()
    assert s.isPalindrome(0) == True
    assert s.isPalindrome(1) == True
    assert s.isPalindrome(22) == True
    assert s.isPalindrome(3223) == True
    assert s.isPalindrome(42224) == True

def test_isPalindrome_false():
    s = Solution()
    assert s.isPalindrome(-1) == False
    assert s.isPalindrome(10) == False
    assert s.isPalindrome(321) == False
    assert s.isPalindrome(123456) == False
    assert s.isPalindrome(1234256789) == False

def test_isPalindrome_error():
    s = Solution()
    with pytest.raises(TypeError):
        s.isPalindrome('12321')
    with pytest.raises(TypeError):
        s.isPalindrome(None)