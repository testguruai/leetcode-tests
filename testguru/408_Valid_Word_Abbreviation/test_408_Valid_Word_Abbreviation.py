import pytest

from solution import Solution

def test_validWordAbbreviation():
    sol = Solution()
    word1 = "internationalization"
    abbr1 = "i12iz4n"
    word2 = "apple"
    abbr2 = "a2e"
    word3 = "dog"
    abbr3 = "d081"
    word4 = "abbreviation"
    abbr4 = "a10n"
    
    assert sol.validWordAbbreviation(word1, abbr1) == True
    assert sol.validWordAbbreviation(word2, abbr2) == True
    assert sol.validWordAbbreviation(word3, abbr3) == False
    assert sol.validWordAbbreviation(word4, abbr4) == True