import pytest


def test_longest_palindrome():
    solution = Solution()
    assert solution.longestPalindrome("abccccdd") == 7
    assert solution.longestPalindrome("aaaabb") == 6
    assert solution.longestPalindrome("abc") == 1
    assert solution.longestPalindrome("") == 0
    assert solution.longestPalindrome("a") == 1
    assert solution.longestPalindrome("bb") == 2
    assert solution.longestPalindrome("bcc") == 3
    assert solution.longestPalindrome("aaa") == 3
    assert solution.longestPalindrome("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 35
    assert solution.longestPalindrome("abcdedcbazyyyzzzyyzyzy") == 19
    assert solution.longestPalindrome("racecar") == 7
    assert solution.longestPalindrome("A man, a plan, a canal: Panama") == 21
    assert solution.longestPalindrome("Was it a car or a cat I saw?") == 13
    assert solution.longestPalindrome("Mr. Owl ate my metal worm") == 13
    assert solution.longestPalindrome("Do geese see God?") == 5 
    assert solution.longestPalindrome("never odd or even") == 15
    assert solution.longestPalindrome("step on no pets") == 11