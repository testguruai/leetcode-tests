# TEST CASES

def test_reverseVowels():
    sol = Solution()

    # Test case with all vowels
    assert sol.reverseVowels("aeiouAEIOU") == "UOIEAuoiea"

    # Test case with no vowels
    assert sol.reverseVowels("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

    # Test case with mixed vowels and consonants
    assert sol.reverseVowels("hello world") == "hollo werld"

    # Test case with uppercase and lowercase vowels
    assert sol.reverseVowels("bEEr IS GooD") == "bOOr IS GiiD"

    # Test case with repeated vowels
    assert sol.reverseVowels("boom") == "boom"

    # Test case with empty string
    assert sol.reverseVowels("") == ""

    # Test case with single vowel
    assert sol.reverseVowels("a") == "a"

    # Test case with single consonant
    assert sol.reverseVowels("b") == "b"

    # Test case with special characters and spaces
    assert sol.reverseVowels("h@!_e^l%l()o w+o*rld") == "h@!_o^l%l()e w+o*rld"