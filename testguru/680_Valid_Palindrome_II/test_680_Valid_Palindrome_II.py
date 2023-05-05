import pytest

def test_validPalindrome():
    s = Solution()
    assert s.validPalindrome("aba") == True
    assert s.validPalindrome("abca") == True
    assert s.validPalindrome("abcda") == False
    assert s.validPalindrome("racecar") == True
    assert s.validPalindrome("") == True
    assert s.validPalindrome("abcdcba") == True
    assert s.validPalindrome("abcdefg") == False
    assert s.validPalindrome("abccbc") == True
    assert s.validPalindrome("abc") == False
    assert s.validPalindrome("abba") == True
    assert s.validPalindrome("a") == True
    assert s.validPalindrome("abbca") == True
    assert s.validPalindrome("abbda") == False
    assert s.validPalindrome("abcdefedcba") == True
    assert s.validPalindrome("babad") == True
    assert s.validPalindrome("cbbd") == True
    assert s.validPalindrome("abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == False