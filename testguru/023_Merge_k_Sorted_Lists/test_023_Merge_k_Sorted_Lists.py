import pytest
from queue import PriorityQueue

from solution import ListNode, Solution

# test case for Priority Queue approach
def testMergeKListsPriorityQueue():
    lists = []
    lists.append(ListNode(1))
    lists[0].next = ListNode(4)
    lists[0].next.next = ListNode(5)

    lists.append(ListNode(1))
    lists[1].next = ListNode(3)
    lists[1].next.next = ListNode(4)

    lists.append(ListNode(2))
    lists[2].next = ListNode(6)

    merged_list = Solution().mergeKLists(lists)

    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.next.val == 5
    assert merged_list.next.next.next.next.next.next.next.val == 6
    assert merged_list.next.next.next.next.next.next.next.next == None

# test case for sort approach
def testMergeKListsSort():
    lists = []
    lists.append(ListNode(1))
    lists[0].next = ListNode(4)
    lists[0].next.next = ListNode(5)

    lists.append(ListNode(1))
    lists[1].next = ListNode(3)
    lists[1].next.next = ListNode(4)

    lists.append(ListNode(2))
    lists[2].next = ListNode(6)

    merged_list = Solution().mergeKLists(lists)

    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.next.val == 5
    assert merged_list.next.next.next.next.next.next.next.val == 6
    assert merged_list.next.next.next.next.next.next.next.next == None

# test case for recursive approach
def testMergeKListsRecursive():
    lists = []
    lists.append(ListNode(1))
    lists[0].next = ListNode(4)
    lists[0].next.next = ListNode(5)

    lists.append(ListNode(1))
    lists[1].next = ListNode(3)
    lists[1].next.next = ListNode(4)

    lists.append(ListNode(2))
    lists[2].next = ListNode(6)

    merged_list = Solution().mergeKLists(lists)

    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.next.val == 5
    assert merged_list.next.next.next.next.next.next.next.val == 6
    assert merged_list.next.next.next.next.next.next.next.next == None

# test case for empty list
def testMergeKListEmptyList():
    lists = []

    merged_list = Solution().mergeKLists(lists)

    assert merged_list == None
