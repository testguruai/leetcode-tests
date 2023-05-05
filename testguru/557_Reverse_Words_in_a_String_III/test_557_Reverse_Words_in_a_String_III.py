import pytest

from solution import Solution

def test_solution():
    sol = Solution()

    # Test 1
    s = "hello world"
    expected = "olleh dlrow"
    assert sol.reverseWords(s) == expected

    # Test 2
    s = "the sky is blue"
    expected = "eht yks si eulb"
    assert sol.reverseWords(s) == expected

    # Test 3
    s = "   hello world   "
    expected = "   olleh dlrow   "
    assert sol.reverseWords(s) == expected

    # Test 4
    s = ""
    expected = ""
    assert sol.reverseWords(s) == expected

    # Test 5
    s = "a"
    expected = "a"
    assert sol.reverseWords(s) == expected

    # Test 6
    s = "   a   "
    expected = "   a   "
    assert sol.reverseWords(s) == expected

    # Test 7
    s = "racecar level noon"
    expected = "racecar level noon"
    assert sol.reverseWords(s) == expected

    # Test 8
    s = "   "
    expected = "   "
    assert sol.reverseWords(s) == expected

    # Test 9
    s = "1 2 3 4 5"
    expected = "1 2 3 4 5"
    assert sol.reverseWords(s) == expected

    # Test 10
    s = "a1b2c3 d4e5f6"
    expected = "3c2b1a 6f5e4d"
    assert sol.reverseWords(s) == expected

    # Test 11
    s = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    expected = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    assert sol.reverseWords(s) == expected

    # Test 12
    s = "     a b c d e f g h i j k l m n o p q r s t u v w x y z     "
    expected = "     a b c d e f g h i j k l m n o p q r s t u v w x y z     "
    assert sol.reverseWords(s) == expected.waitKey(0)