import pytest
from solution import Solution, ListNode


def create_linked_list(nums):
    head = None
    current = None
    for num in nums:
        node = ListNode(num)
        if not current:
            head = current = node
        else:
            current.next = node
            current = node
    return head


def linked_lists_equal(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True


class TestAddTwoNumbers:
    def test_base_case(self):
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        expected = create_linked_list([7, 0, 8])
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert linked_lists_equal(result, expected)

    def test_zeros(self):
        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        expected = create_linked_list([0])
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert linked_lists_equal(result, expected)

    def test_different_length(self):
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4, 2, 1])
        expected = create_linked_list([7, 0, 8, 2, 1])
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert linked_lists_equal(result, expected)

    def test_carry_over(self):
        l1 = create_linked_list([9, 9, 9])
        l2 = create_linked_list([1, 0, 0])
        expected = create_linked_list([0, 0, 0, 1])
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert linked_lists_equal(result, expected)

    def test_empty_lists(self):
        l1 = None
        l2 = None
        expected = None
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert linked_lists_equal(result, expected)
