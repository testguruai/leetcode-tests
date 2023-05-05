import pytest

# create test cases
test_cases = [
    ("", "", True),
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
]

# Define fixture to create a Solution object
@pytest.fixture
def solution():
    return Solution()

# Define test function
def test_isMatch(solution, inputs, expected):
    s, p = inputs
    assert solution.isMatch(s, p) == expected

# use pytest.mark.parametrize to run multiple test cases with the same test function
@pytest.mark.parametrize("inputs,expected", test_cases)
def test_multiple_cases(solution, inputs, expected):
    test_isMatch(solution, inputs, expected)