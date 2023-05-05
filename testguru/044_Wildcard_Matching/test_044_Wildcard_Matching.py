
def test_isMatch1():
    s = Solution()
    assert s.isMatch("aa", "a") == False

def test_isMatch2():
    s = Solution()
    assert s.isMatch("aa", "*") == True
    
def test_isMatch3():
    s = Solution()
    assert s.isMatch("cb", "?a") == False
    
def test_isMatch4():
    s = Solution()
    assert s.isMatch("adceb", "*a*b") == True
    
def test_isMatch5():
    s = Solution()
    assert s.isMatch("acdcb", "a*c?b") == False
