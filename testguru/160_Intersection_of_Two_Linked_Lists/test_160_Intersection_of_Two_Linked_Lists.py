import pytest

from solution import ListNode, Solution

def create_linked_list(vals):
    head = None
    prev = None
    for val in vals:
        node = ListNode(val)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head


def test_getIntersectionNode():
    solution = Solution()

    # Case 1: No intersecting nodes
    headA = create_linked_list([1, 2, 3])
    headB = create_linked_list([4, 5, 6])
    assert solution.getIntersectionNode(headA, headB) is None

    # Case 2: Intersecting nodes
    intersection = create_linked_list([7, 8, 9])
    headA = create_linked_list([1, 2, 3])
    headA.next.next.next = intersection
    headB = create_linked_list([4, 5, 6])
    headB.next.next = intersection
    assert solution.getIntersectionNode(headA, headB) == intersection

    # Case 3: Identical linked lists
    headA = create_linked_list([1, 2, 3])
    headB = headA
    assert solution.getIntersectionNode(headA, headB) == headA

    # Case 4: One list is a sublist of the other list
    headA = create_linked_list([1, 2, 3, 4, 5, 6])
    headB = create_linked_list([3, 4, 5])
    assert solution.getIntersectionNode(headA, headB) == headB