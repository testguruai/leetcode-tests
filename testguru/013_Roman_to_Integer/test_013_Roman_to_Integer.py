import pytest

class TestSolution:
    def test_romanToInt_I(self):
        s = Solution()
        assert s.romanToInt('I') == 1
    
    def test_romanToInt_V(self):
        s = Solution()
        assert s.romanToInt('V') == 5
    
    def test_romanToInt_IV(self):
        s = Solution()
        assert s.romanToInt('IV') == 4
    
    def test_romanToInt_IX(self):
        s = Solution()
        assert s.romanToInt('IX') == 9
    
    def test_romanToInt_XL(self):
        s = Solution()
        assert s.romanToInt('XL') == 40
    
    def test_romanToInt_CMIX(self):
        s = Solution()
        assert s.romanToInt('CMIX') == 909
    
    def test_romanToInt_MMMCMXCIX(self):
        s = Solution()
        assert s.romanToInt('MMMCMXCIX') == 3999