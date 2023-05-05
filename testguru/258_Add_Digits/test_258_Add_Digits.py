import pytest

from solution import Solution

def test_addDigits():
    sol = Solution()

    # Test case 1
    assert sol.addDigits(38) == 2

    # Test case 2
    assert sol.addDigits(0) == 0

    # Test case 3
    assert sol.addDigits(9) == 9

    # Test case 4
    assert sol.addDigits(1234) == 1

    # Test case 5
    assert sol.addDigits(11111) == 5

    # Test case 6
    assert sol.addDigits(99999) == 9

    # Test case 7
    assert sol.addDigits(98765432) == 6

    # Test case 8
    assert sol.addDigits(123456789) == 9

    # Test case 9
    assert sol.addDigits(444) == 3

    # Test case 10
    assert sol.addDigits(987654) == 3

    # Test case 11
    assert sol.addDigits(-123) == None

    # Test case 12
    assert sol.addDigits("abc") == None

    # Test case 13
    assert sol.addDigits(10.5) == None

    # Test case 14
    assert sol.addDigits(9999999999999999999999999999999999) == 9

    # Test case 15
    assert sol.addDigits(10000000000000000000000000000000000) == 1

    # Test case 16
    assert sol.addDigits(1) == 1

    # Test case 17
    assert sol.addDigits(101) == 2

    # Test case 18
    assert sol.addDigits(102) == 3

    # Test case 19
    assert sol.addDigits(103) == 4

    # Test case 20
    assert sol.addDigits(999999999999999999999999999998) == 8

    # Test case 21
    assert sol.addDigits(99999999999999999999999999999) == 9

    # Test case 22
    assert sol.addDigits(123456789012345678901234567890) == 9

    # Test case 23
    assert sol.addDigits(12345678901234567890123456789) == 2

    # Test case 24
    assert sol.addDigits(123456789012345678901234567891) == 3

    # Test case 25
    assert sol.addDigits(123456789012345678901234567892) == 4