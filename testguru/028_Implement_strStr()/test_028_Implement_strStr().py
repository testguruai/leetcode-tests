import pytest

class TestSolution:

    def test_strStr_empty_needle(self):
        s = Solution()
        assert s.strStr("hello", "") == 0

    def test_strStr_no_match(self):
        s = Solution()
        assert s.strStr("hello", "world") == -1

    def test_strStr_single_char_haystack(self):
        s = Solution()
        assert s.strStr("h", "h") == 0

    def test_strStr_multiple_matches(self):
        s = Solution()
        assert s.strStr("mississippi", "issi") == 1

    def test_strStr_match_at_end(self):
        s = Solution()
        assert s.strStr("hello", "lo") == 3

    def test_makeNext(self):
        s = Solution()
        assert s.makeNext("abababca") == [-1, 0, 0, 1, 2, 3, 0, 1]

    def test_makeNext_empty_needle(self):
        s = Solution()
        assert s.makeNext("") == []

    def test_makeNext_single_char_needle(self):
        s = Solution()
        assert s.makeNext("a") == [-1]