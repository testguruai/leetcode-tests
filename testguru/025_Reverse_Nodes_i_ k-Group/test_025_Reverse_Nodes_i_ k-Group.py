import pytest

from solution import Solution, ListNode


def create_linked_list(nums):
    """
    Create a singly-linked list based on an array of integers.

    :param nums: list of integers
    :return: the head of the linked list
    """
    if not nums:
        return None

    head = ListNode(nums[0])
    curr = head

    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head


def linked_list_to_list(head):
    """
    Convert a singly-linked list to an array of integers.

    :param head: the head of the linked list
    :return: list of integers
    """
    nums = []
    curr = head

    while curr:
        nums.append(curr.val)
        curr = curr.next

    return nums


class TestSolution:
    def test_reverseKGroup(self):
        solution = Solution()

        # test case where list is empty
        assert solution.reverseKGroup(None, 2) is None

        # test case where k is 1
        head = create_linked_list([1, 2, 3, 4])
        assert linked_list_to_list(solution.reverseKGroup(head, 1)) == [1, 2, 3, 4]

        # test case where there are not enough nodes to reverse
        head = create_linked_list([1, 2, 3, 4, 5])
        assert linked_list_to_list(solution.reverseKGroup(head, 6)) == [1, 2, 3, 4, 5]

        # test case where number of nodes is divisible by k
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        assert linked_list_to_list(solution.reverseKGroup(head, 2)) == [2, 1, 4, 3, 6, 5]

        # test case where number of nodes is not divisible by k
        head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
        assert linked_list_to_list(solution.reverseKGroup(head, 3)) == [3, 2, 1, 6, 5, 4, 7]