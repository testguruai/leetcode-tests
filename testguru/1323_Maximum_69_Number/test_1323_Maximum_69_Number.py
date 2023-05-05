
import pytest
from solution import Solution

def test_given_example_1():
    s = Solution()
    num = 9669
    assert s.maximum69Number(num) == '9969'

def test_given_example_2():
    s = Solution()
    num = 9996
    assert s.maximum69Number(num) == '9999'

def test_only_6():
    s = Solution()
    num = 6
    assert s.maximum69Number(num) == '9'

def test_only_9():
    s = Solution()
    num = 9
    assert s.maximum69Number(num) == '9'

def test_no_6():
    s = Solution()
    num = 1234567890
    assert s.maximum69Number(num) == '1234567890'

def test_many_6():
    s = Solution()
    num = 666666666
    assert s.maximum69Number(num) == '966666666'

def test_negative_input():
    s = Solution()
    num = -666
    with pytest.raises(ValueError):
        s.maximum69Number(num)

def test_non_integer_input():
    s = Solution()
    num = '123'
    with pytest.raises(TypeError):
        s.maximum69Number(num)
