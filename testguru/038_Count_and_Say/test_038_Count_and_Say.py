import pytest

from .solution import Solution


class TestSolution:
    def test_countAndSay_1(self):
        s = Solution()
        assert s.countAndSay(1) == '1'

    def test_countAndSay_2(self):
        s = Solution()
        assert s.countAndSay(2) == '11'

    def test_countAndSay_3(self):
        s = Solution()
        assert s.countAndSay(3) == '21'

    def test_countAndSay_4(self):
        s = Solution()
        assert s.countAndSay(4) == '1211'

    def test_countAndSay_5(self):
        s = Solution()
        assert s.countAndSay(5) == '111221'

    def test_countAndSay_6(self):
        s = Solution()
        assert s.countAndSay(6) == '312211'

    def test_countAndSay_7(self):
        s = Solution()
        assert s.countAndSay(7) == '13112221'

    def test_countAndSay_8(self):
        s = Solution()
        assert s.countAndSay(8) == '1113213211'

    def test_countAndSay_9(self):
        s = Solution()
        assert s.countAndSay(9) == '31131211131221'