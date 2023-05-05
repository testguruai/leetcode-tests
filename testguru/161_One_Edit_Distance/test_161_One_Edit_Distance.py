# Import the class to be tested
from solution import Solution

# Initialize the class object
solution = Solution()

# Test case 1
def test_isOneEditDistance_1():
    assert solution.isOneEditDistance("abcd", "abccd") == True
    
# Test case 2
def test_isOneEditDistance_2():
    assert solution.isOneEditDistance("abcde", "abcd") == True
    
# Test case 3
def test_isOneEditDistance_3():
    assert solution.isOneEditDistance("abc", "abcdd") == False
    
# Test case 4
def test_isOneEditDistance_4():
    assert solution.isOneEditDistance("", "") == False
    
# Test case 5
def test_isOneEditDistance_5():
    assert solution.isOneEditDistance("", "a") == True
    
# Test case 6
def test_isOneEditDistance_6():
    assert solution.isOneEditDistance("abcd", "dcba") == False
    
# Test case 7
def test_isOneEditDistance_7():
    assert solution.isOneEditDistance("abck", "abcf") == True
    
# Test case 8
def test_isOneEditDistance_8():
    assert solution.isOneEditDistance("abcde", "abfde") == True
    
# Test case 9
def test_isOneEditDistance_9():
    assert solution.isOneEditDistance("a", "") == True
    
# Test case 10
def test_isOneEditDistance_10():
    assert solution.isOneEditDistance("abc", "abc") == False
    
    
# Run the tests
test_isOneEditDistance_1()
test_isOneEditDistance_2()
test_isOneEditDistance_3()
test_isOneEditDistance_4()
test_isOneEditDistance_5()
test_isOneEditDistance_6()
test_isOneEditDistance_7()
test_isOneEditDistance_8()
test_isOneEditDistance_9()
test_isOneEditDistance_10()