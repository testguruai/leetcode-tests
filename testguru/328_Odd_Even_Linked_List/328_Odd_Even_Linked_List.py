# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        if head is None:
            return None
        if head.__next__ is None:
            return head
        even_head = even = head.__next__
        while odd.__next__ is not None and even.__next__ is not None:
            odd.next = even.__next__
            odd = odd.__next__
            even.next = odd.__next__
            even = even.__next__
        odd.next = even_head
        return head

    # def oddEvenList(self, head):
    #     # slicing
    #     if (head != None):
    #         x = []
    #     else:
    #         return []
    #     while (head.next != None):
    #         x.append(head.val)
    #         head = head.next
    #     x.append(head.val)
    #     return x[0::2] + x[1::2]