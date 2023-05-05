import pytest
from .solution import Solution, ListNode

def create_linkedlist_from_list(a: list) -> ListNode:
    head = ListNode(-1)
    node = head
    for val in a:
        node.next = ListNode(val)
        node = node.next
    return head.next

def create_list_from_linkedlist(node: ListNode) -> list:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def test_swapPairs():
    s = Solution()

    # Test case 1
    head = create_linkedlist_from_list([1,2,3,4])
    expected_output = [2,1,4,3]
    assert create_list_from_linkedlist(s.swapPairs(head)) == expected_output

    # Test case 2
    head = create_linkedlist_from_list([1])
    expected_output = [1]
    assert create_list_from_linkedlist(s.swapPairs(head)) == expected_output

    # Test case 3
    head = create_linkedlist_from_list([])
    expected_output = []
    assert create_list_from_linkedlist(s.swapPairs(head)) == expected_output

    # Test case 4
    head = create_linkedlist_from_list([1,2,3])
    expected_output = [2,1,3]
    assert create_list_from_linkedlist(s.swapPairs(head)) == expected_output

    # Test case 5
    head = create_linkedlist_from_list([1,2,3,4,5,6])
    expected_output = [2,1,4,3,6,5]
    assert create_list_from_linkedlist(s.swapPairs(head)) == expected_output

    # Test case 6
    head = None
    expected_output = None
    assert s.swapPairs(head) == expected_output