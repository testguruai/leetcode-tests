import pytest


def test_reverseList_iteratively():
    # test case 1
    s = Solution()
    head = None
    assert s.reverseList(head) is None

    # test case 2
    s = Solution()
    head = ListNode(1)
    assert s.reverseList(head) == head

    # test case 3
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    expected = ListNode(3)
    expected.next = ListNode(2)
    expected.next.next = ListNode(1)
    assert s.reverseList(head) == expected


def test_reverseList_recursively():
    # test case 1
    s = Solution()
    head = None
    assert s.reverseList(head) is None

    # test case 2
    s = Solution()
    head = ListNode(1)
    assert s.reverseList(head) == head

    # test case 3
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    expected = ListNode(3)
    expected.next = ListNode(2)
    expected.next.next = ListNode(1)
    assert s.reverseList(head) == expected