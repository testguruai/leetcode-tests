
import pytest
from solution import Solution


class TestSolution:
    def test_numJewelsInStones(self):
        s = Solution()
        assert s.numJewelsInStones("aA", "aAAbbbb") == 3
        assert s.numJewelsInStones("z", "ZZZZ") == 0
        assert s.numJewelsInStones("", "anything") == 0
        assert s.numJewelsInStones("anything", "") == 0
        assert s.numJewelsInStones("", "") == 0
        assert s.numJewelsInStones("abc", "abcdefg") == 3
        assert s.numJewelsInStones("AbC", "aAbBcC") == 6
