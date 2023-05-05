import pytest
from solution import Solution, ListNode

def create_linked_list_from_list(nums):
    """
    Helper function to create a linked list from a list of numbers
    """
    dummy = ListNode(-1)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def create_list_from_linked_list(head):
    """
    Helper function to create a list from a linked list
    """
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def test_plusOne():
    s = Solution()

    # Test Case 1
    head = create_linked_list_from_list([1, 2, 3])
    new_head = s.plusOne(head)
    assert create_list_from_linked_list(new_head) == [1, 2, 4]

    # Test Case 2
    head = create_linked_list_from_list([9, 9, 9])
    new_head = s.plusOne(head)
    assert create_list_from_linked_list(new_head) == [1, 0, 0, 0]

    # Test Case 3
    head = create_linked_list_from_list([0])
    new_head = s.plusOne(head)
    assert create_list_from_linked_list(new_head) == [1]