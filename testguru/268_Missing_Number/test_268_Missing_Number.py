import pytest
import solution

def test_missingNumber_1():
    s = Solution()
    assert s.missingNumber([0, 1, 3]) == 2

def test_missingNumber_2():
    s = Solution()
    assert s.missingNumber([1, 2, 3, 4, 6]) == 0

def test_missingNumber_3():
    s = Solution()
    assert s.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 10

def test_missingNumber_4():
    s = Solution()
    assert s.missingNumber([0]) == 1

def test_missingNumber_5():
    s = Solution()
    assert s.missingNumber([1]) == 0

def test_missingNumber_6():
    s = Solution()
    assert s.missingNumber([]) == 0

def test_missingNumber_7():
    s = Solution()
    assert s.missingNumber([0, 1, 2]) == 3

def test_missingNumber_8():
    s = Solution()
    assert s.missingNumber([1, 2, 3]) == 0

def test_missingNumber_9():
    s = Solution()
    assert s.missingNumber([0, 2, 3]) == 1

def test_missingNumber_10():
    s = Solution()
    assert s.missingNumber([0, 1]) == 2

def test_missingNumber_11():
    s = Solution()
    assert s.missingNumber([1, 3]) == 0

def test_missingNumber_12():
    s = Solution()
    assert s.missingNumber([2, 3]) == 0

def test_missingNumber_13():
    s = Solution()
    assert s.missingNumber([1, 2]) == 0

def test_missingNumber_14():
    s = Solution()
    assert s.missingNumber([0, 2]) == 1

def test_missingNumber_15():
    s = Solution()
    assert s.missingNumber([0]) == 1
