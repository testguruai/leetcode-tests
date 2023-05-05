import pytest

from solution import Solution

def test_empty_string():
    s = Solution()
    assert s.isNumber("") == False
    
def test_only_spaces():
    s = Solution()
    assert s.isNumber("    ") == False
    
def test_integer():
    s = Solution()
    assert s.isNumber("123") == True
    
def test_negative_integer():
    s = Solution()
    assert s.isNumber("-123") == True
    
def test_float():
    s = Solution()
    assert s.isNumber("123.456") == True
    
def test_negative_float():
    s = Solution()
    assert s.isNumber("-123.456") == True
    
def test_exponential_notation():
    s = Solution()
    assert s.isNumber("1e3") == True
    
def test_negative_exponential_notation():
    s = Solution()
    assert s.isNumber("-1e3") == True
    
def test_mixed_notation():
    s = Solution()
    assert s.isNumber("1.23e4") == True
    
def test_invalid_number_1():
    s = Solution()
    assert s.isNumber("abc") == False
    
def test_invalid_number_2():
    s = Solution()
    assert s.isNumber("123a") == False
    
def test_invalid_number_3():
    s = Solution()
    assert s.isNumber("12 3") == False
    
def test_invalid_number_4():
    s = Solution()
    assert s.isNumber("12.4.5") == False
    
def test_invalid_number_5():
    s = Solution()
    assert s.isNumber("-") == False
    
def test_invalid_number_6():
    s = Solution()
    assert s.isNumber("1.2.e3") == False