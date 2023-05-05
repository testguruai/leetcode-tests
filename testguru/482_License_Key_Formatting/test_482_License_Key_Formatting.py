import pytest

from solution import Solution

def test_licenseKeyFormatting():
    solution = Solution()

    # Test case where S is empty string
    assert solution.licenseKeyFormatting("", 4) == ""

    # Test case where S contains only one character
    assert solution.licenseKeyFormatting("a", 4) == "A"

    # Test case where S contains only hyphens
    assert solution.licenseKeyFormatting("---", 4) == ""

    # Test case where K is larger than the length of S
    assert solution.licenseKeyFormatting("abc", 4) == "ABC"

    # Test case where S contains only one block of characters
    assert solution.licenseKeyFormatting("abcd", 4) == "ABCD"

    # Test case where S contains multiple blocks of characters and K is a factor of the length of S
    assert solution.licenseKeyFormatting("ab-cd-ef", 2) == "AB-CD-EF"

    # Test case where S contains multiple blocks of characters and K is not a factor of the length of S
    assert solution.licenseKeyFormatting("abc-defg-hij", 4) == "ABCD-EFGH-IJ"
    
    # Test case where S contains hyphens and K is larger than the length of each non-hyphen block
    assert solution.licenseKeyFormatting("a-b-c-d", 6) == "A-B-C-D"