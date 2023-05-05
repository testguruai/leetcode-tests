import pytest

class TestSolution:
    def test_n_th_ugly_number(self):
        s = Solution()
        assert s.nthUglyNumber(1) == 1
        assert s.nthUglyNumber(2) == 2
        assert s.nthUglyNumber(3) == 3
        assert s.nthUglyNumber(4) == 4
        assert s.nthUglyNumber(5) == 5
        assert s.nthUglyNumber(6) == 6
        assert s.nthUglyNumber(7) == 8
        assert s.nthUglyNumber(8) == 9
        assert s.nthUglyNumber(9) == 10
        assert s.nthUglyNumber(10) == 12
        assert s.nthUglyNumber(11) == 15
        assert s.nthUglyNumber(12) == 16
        assert s.nthUglyNumber(13) == 18
        assert s.nthUglyNumber(14) == 20
        assert s.nthUglyNumber(15) == 24
        assert s.nthUglyNumber(16) == 25
        assert s.nthUglyNumber(17) == 27
        assert s.nthUglyNumber(18) == 30
        assert s.nthUglyNumber(19) == 32
        assert s.nthUglyNumber(20) == 36

if __name__ == '__main__':
    pytest.main()