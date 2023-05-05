# Test Cases for removeElements method in Solution class

from solution import Solution


def test_removeElements_empty_list():
    # Empty list should return None
    s = Solution()
    assert s.removeElements(None, 2) == None


def test_removeElements_remove_all_elements():
    # Removing all occurrences of element from list
    # should return None
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    assert s.removeElements(head, 2) == None


def test_removeElements_remove_head():
    # Removing head element from list
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(3)
    assert s.removeElements(head, 2).val == 3


def test_removeElements_remove_middle_element():
    # Removing middle element from list
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    assert s.removeElements(head, 4).next.val == 3


def test_removeElements_remove_last_element():
    # Removing last element from list
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    assert s.removeElements(head, 3).next.next == None


def test_removeElements_no_element_to_remove():
    # List does not contain the element to remove
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    assert s.removeElements(head, 5).next.next.val == 3