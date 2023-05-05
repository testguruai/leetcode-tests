import pytest

from solution import Solution, ListNode

def test_rotateRight():
    # Test Case 1
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    k = 2
    s = Solution()
    result = s.rotateRight(head, k)
    assert result.val == 4
    assert result.next.val == 5
    assert result.next.next.val == 1
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 3
    assert result.next.next.next.next.next is None

    # Test Case 2
    head = ListNode(0)
    k = 0
    s = Solution()
    result = s.rotateRight(head, k)
    assert result.val == 0
    assert result.next is None

    # Test Case 3
    head = ListNode(1)
    k = 1
    s = Solution()
    result = s.rotateRight(head, k)
    assert result.val == 1
    assert result.next is None

    # Test Case 4
    head = None
    k = 5
    s = Solution()
    result = s.rotateRight(head, k)
    assert result is None

    # Test Case 5
    head = ListNode(1)
    k = 10
    s = Solution()
    result = s.rotateRight(head, k)
    assert result.val == 1
    assert result.next is None