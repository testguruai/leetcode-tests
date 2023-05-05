# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        place_stop, tail = dummy, dummy
        # find the tail
        while tail.__next__ is not None:
            tail = tail.__next__
            if tail.val != 9:
                place_stop = tail
        if tail.val != 9:
            # done
            tail.val += 1
        else:
            # not yet
            place_stop.val += 1
            place_stop = place_stop.__next__
            # set all node behind this place to zero
            while place_stop is not None:
                place_stop.val = 0
                place_stop = place_stop.__next__
        if dummy.val == 0:
            return dummy.__next__
        return dummy
