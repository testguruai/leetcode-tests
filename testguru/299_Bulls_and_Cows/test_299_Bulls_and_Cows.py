import pytest

@pytest.fixture()
def solution():
    return Solution()

def test_getHint(solution):
    assert solution.getHint("1122", "1222") == "3A0B"
    assert solution.getHint("1234", "0111") == "0A1B"
    assert solution.getHint("4321", "1234") == "0A4B"
    assert solution.getHint("1111", "1111") == "4A0B"
    assert solution.getHint("2468", "8642") == "0A4B"
    assert solution.getHint("2468", "2468") == "4A0B" 

def test_getHint_empty_string(solution):
    assert solution.getHint("", "") == "0A0B"
    assert solution.getHint("", "1234") == "0A0B"
    assert solution.getHint("1234", "") == "0A0B"

def test_getHint_different_length(solution):
    with pytest.raises(ValueError):
        assert solution.getHint("123", "12345")
    with pytest.raises(ValueError):
        assert solution.getHint("12345", "123") 
    
def test_getHint_same_string(solution):
    assert solution.getHint("1234", "1234") == "4A0B"