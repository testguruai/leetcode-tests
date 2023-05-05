import pytest

class TestSolution:
    def test_isScramble_basic(self):
        s = Solution()
        assert s.isScramble("abc", "bca") == True
        assert s.isScramble("abc", "cba") == True
        assert s.isScramble("abc", "cab") == True
        assert s.isScramble("cat", "tca") == True
        assert s.isScramble("eat", "tae") == True
        assert s.isScramble("ab", "ba") == True
        assert s.isScramble("a", "a") == True
        assert s.isScramble("b", "b") == True
        assert s.isScramble("ab", "ab") == True
        assert s.isScramble("aab", "aba") == True
        assert s.isScramble("great", "rgeat") == True

    def test_isScramble_edge_cases(self):
        s = Solution()
        assert s.isScramble("", "") == True
        assert s.isScramble("a", "b") == False
        assert s.isScramble("a", "") == False
        assert s.isScramble("", "a") == False
        assert s.isScramble("abcdefg", "gfedcba") == False

    def test_isScramble_memoization(self):
        s = Solution()
        # Same as basic tests, but with memoization
        assert s.isScramble("", "") == True
        assert s.isScramble("abc", "bca") == True
        memo = {}
        assert s.isScramble("abc", "cba", memo) == True
        assert memo[("abc", "cba")] == True
        assert s.isScramble("abc", "cab", memo) == True
        assert memo[("abc", "cab")] == True
        assert s.isScramble("cat", "tca", memo) == True
        assert memo[("cat", "tca")] == True
        assert s.isScramble("eat", "tae", memo) == True
        assert memo[("eat", "tae")] == True
        assert s.isScramble("ab", "ba", memo) == True
        assert memo[("ab", "ba")] == True
        assert s.isScramble("a", "a", memo) == True
        assert memo[("a", "a")] == True
        assert s.isScramble("b", "b", memo) == True
        assert memo[("b", "b")] == True
        assert s.isScramble("ab", "ab", memo) == True
        assert memo[("ab", "ab")] == True
        assert s.isScramble("aab", "aba", memo) == True
        assert memo[("aab", "aba")] == True
        assert s.isScramble("great", "rgeat", memo) == True
        assert memo[("great", "rgeat")] == True

    def test_isScramble_invalid_inputs(self):
        s = Solution()
        with pytest.raises(TypeError):
            s.isScramble(123, "abc")
        with pytest.raises(TypeError):
            s.isScramble("abc", 123)
        with pytest.raises(TypeError):
            s.isScramble(123, 123)