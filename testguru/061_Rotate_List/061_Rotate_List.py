# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while k and fast.__next__:
            fast = fast.__next__
            length += 1
            k -= 1

        if k != 0:
            k = (k + length - 1) % length # original k % length
            return self.rotateRight(head, k)
        else:
            while fast.__next__:
                fast = fast.__next__
                slow = slow.__next__
            return self.rotate(head, fast, slow)

    def rotate(self, head, fast, slow):
        fast.next = head
        head = slow.__next__
        slow.next = None
        return head