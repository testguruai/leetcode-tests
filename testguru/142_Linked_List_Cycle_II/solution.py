# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Two points
        # https://discuss.leetcode.com/topic/2975/o-n-solution-by-using-two-pointers-without-change-anything
        try:
            fast = head.next.__next__
            slow = head.__next__

            while fast != slow:
                fast = fast.next.__next__
                slow = slow.__next__
        except:
            return None
        slow = head
        while fast != slow:
            fast = fast.__next__
            slow = slow.__next__
        return fast

