import pytest
from solution import Solution
from solution import ListNode

def test_insertionSortList():

    # Test case 1
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    solution = Solution()
    sorted_head = solution.insertionSortList(head)

    assert sorted_head.val == 1
    assert sorted_head.next.val == 2
    assert sorted_head.next.next.val == 3
    assert sorted_head.next.next.next.val == 4
    assert sorted_head.next.next.next.next == None

    # Test case 2
    head = None

    solution = Solution()
    sorted_head = solution.insertionSortList(head)

    assert sorted_head == None

    # Test case 3
    head = ListNode(1)

    solution = Solution()
    sorted_head = solution.insertionSortList(head)

    assert sorted_head.val == 1
    assert sorted_head.next == None
