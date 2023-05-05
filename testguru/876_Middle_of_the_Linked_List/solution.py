# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def middleNode(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     res = []
    #     while head:
    #         res.append(head)
    #         head = head.next
    #     return res[len(res) / 2]

    def middleNode(self, head):
        # Fast point is 2 times faster than slow point
        fast = slow = head
        while fast and fast.__next__:
            slow = slow.__next__
            fast = fast.next.__next__
        return slow
