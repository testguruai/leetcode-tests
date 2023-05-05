@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("s, expected", [
    ("", True),
    ("aba", True),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("12321", True),
    ("abbc", False)
])
def test_isPalindrome(solution, s, expected):
    assert solution.isPalindrome(s) == expected

def test_isPalindrome_returns_bool(solution):
    assert isinstance(solution.isPalindrome(""), bool) == True

def test_isPalindrome_with_spaces_in_between_returns_true(solution):
    assert solution.isPalindrome("a   b A") == True

def test_isPalindrome_with_odd_length_returns_true(solution):
    assert solution.isPalindrome("racecar") == True

def test_isPalindrome_with_odd_length_returns_false(solution):
    assert solution.isPalindrome("notapalindrome") == False

def test_isPalindrome_with_even_length_returns_true(solution):
    assert solution.isPalindrome("abba") == True

def test_isPalindrome_with_even_length_returns_false(solution):
    assert solution.isPalindrome("hello") == False