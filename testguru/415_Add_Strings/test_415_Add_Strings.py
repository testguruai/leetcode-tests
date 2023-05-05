import pytest 

def test_addStrings():
    # test case 1
    s = Solution()
    num1 = "11"
    num2 = "123"
    assert s.addStrings(num1, num2) == "134"

    # test case 2
    s = Solution()
    num1 = "999"
    num2 = "1"
    assert s.addStrings(num1, num2) == "1000"

    # test case 3
    s = Solution()
    num1 = "0"
    num2 = "0"
    assert s.addStrings(num1, num2) == "0"

    # test case 4
    s = Solution()
    num1 = "9999"
    num2 = "1"
    assert s.addStrings(num1, num2) == "10000"