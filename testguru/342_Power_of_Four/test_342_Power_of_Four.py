
def test_is_power_of_four_true():
    sol = Solution()
    assert sol.isPowerOfFour(1) == True
    assert sol.isPowerOfFour(4) == True
    assert sol.isPowerOfFour(16) == True
    assert sol.isPowerOfFour(64) == True

def test_is_power_of_four_false():
    sol = Solution()
    assert sol.isPowerOfFour(0) == False
    assert sol.isPowerOfFour(2) == False
    assert sol.isPowerOfFour(7) == False
    assert sol.isPowerOfFour(15) == False
    assert sol.isPowerOfFour(-4) == False
