import pytest

def test_getDecimalValue():
    # Test case 1
    assert Solution().getDecimalValue(ListNode([1, 0, 1])) == 5

    # Test case 2
    assert Solution().getDecimalValue(ListNode([0])) == 0

    # Test case 3
    assert Solution().getDecimalValue(ListNode([1])) == 1

    # Test case 4
    assert Solution().getDecimalValue(ListNode([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880

    # Test case 5
    assert Solution().getDecimalValue(ListNode([0, 0])) == 0