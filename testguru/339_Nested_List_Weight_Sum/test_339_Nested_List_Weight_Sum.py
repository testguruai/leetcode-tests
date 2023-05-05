import pytest

# First, create tests for the isInteger() method of NestedInteger
def test_isInteger_returns_true_for_single_integer_ni():
    ni = NestedInteger()
    ni.setInteger(5)
    assert ni.isInteger() == True

def test_isInteger_returns_false_for_nested_list_ni():
    ni = NestedInteger()
    ni.setList([NestedInteger(), NestedInteger()])
    assert ni.isInteger() == False

# Next, create tests for the getInteger() method of NestedInteger
def test_getInteger_returns_integer_for_single_integer_ni():
    ni = NestedInteger()
    ni.setInteger(5)
    assert ni.getInteger() == 5

def test_getInteger_returns_none_for_nested_list_ni():
    ni = NestedInteger()
    ni.setList([NestedInteger(), NestedInteger()])
    assert ni.getInteger() == None

# Finally, create tests for the getList() method of NestedInteger
def test_getList_returns_list_for_nested_list_ni():
    ni = NestedInteger()
    ni.setList([NestedInteger(), NestedInteger()])
    assert isinstance(ni.getList(), list)

def test_getList_returns_none_for_single_integer_ni():
    ni = NestedInteger()
    ni.setInteger(5)
    assert ni.getList() == None

# Now, create tests for the Solution class
def test_depthSum_returns_correct_sum_for_single_integer_list():
    solution = Solution()
    ni = NestedInteger()
    ni.setInteger(5)
    nested_list = [ni]
    assert solution.depthSum(nested_list) == 5

def test_depthSum_returns_correct_sum_for_nested_list():
    solution = Solution()
    ni1 = NestedInteger()
    ni1.setInteger(1)
    ni2 = NestedInteger()
    ni2.setList([NestedInteger(), NestedInteger()])
    ni3 = NestedInteger()
    ni3.setInteger(3)
    nested_list = [ni1, ni2, ni3]
    assert solution.depthSum(nested_list) == 4