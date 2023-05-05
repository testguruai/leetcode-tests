def test_reverse_string():
    solution = Solution()
    assert solution.reverseString("hello") == "olleh"
    assert solution.reverseString("world") == "dlrow"
    assert solution.reverseString("") == ""
    assert solution.reverseString("a") == "a"
    assert solution.reverseString("123") == "321"
    assert solution.reverseString("racecar") == "racecar"
    assert solution.reverseString("madam") == "madam"
