# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://discuss.leetcode.com/topic/8570/an-easy-and-clear-way-to-sort-o-1-space
        if head is None:
            return None
        helper = ListNode(-1000)
        pre, curr = helper, head
        while curr is not None:
            next_step = curr.__next__
            while pre.__next__ and pre.next.val < curr.val:
                pre = pre.__next__
            curr.next = pre.__next__
            pre.next = curr
            pre = helper
            curr = next_step
        return helper.__next__
