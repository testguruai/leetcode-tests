import pytest

class TestSolution:
    def test_read1(self):
        s = Solution()
        buf = [''] * 6
        assert s.read(buf, 3) == 3
        assert buf[:3] == ['a', 'b', 'c']

    def test_read2(self):
        s = Solution()
        buf = [''] * 6
        assert s.read(buf, 6) == 6
        assert buf == ['a', 'b', 'c', 'd', 'e', 'f']

    def test_read3(self):
        s = Solution()
        buf = [''] * 10
        assert s.read(buf, 8) == 8
        assert buf[:8] == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def test_read4(self):
        s = Solution()
        buf = [''] * 4
        assert s.read(buf, 3) == 3
        assert buf == ['a', 'b', 'c', '']

    def test_read5(self):
        s = Solution()
        buf = [''] * 1
        assert s.read(buf, 1) == 1
        assert buf == ['a']