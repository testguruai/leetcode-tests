# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     # hash O(n) and O(n)
    #     dic = collections.defaultdict(lambda: RandomListNode(0))
    #     dic[None] = None
    #     n = head
    #     while n:
    #         dic[n].label = n.label
    #         dic[n].next = dic[n.next]
    #         dic[n].random = dic[n.random]
    #         n = n.next
    #     return dic[head]

    # def copyRandomList(self, head):
    #     # hash O(n) and O(n)
    #     dic = {}
    #     dic[None] = None
    #     dummyHead = RandomListNode(0)
    #     p, q = head, dummyHead
    #     while p is not None:
    #         q.next = RandomListNode(p.label)
    #         dic[p] = q.next
    #         p = p.next
    #         q = q.next
    #     p, q = head, dummyHead
    #     while p is not None:
    #         q.next.random = dic[p.random]
    #         p = p.next
    #         q = q.next
    #     return dummyHead.next

    def copyRandomList(self, head):
        # Modify original structure: Original->Copy->Original->Copy
        # node.next.random = node.random.next
        # O(n) and O(1)
        p = head
        while p is not None:
            next = p.__next__
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next =  next
            p = next
        p = head
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.__next__
            p = p.next.__next__
        p = head
        if p is not None:
            headCopy = p.__next__
        else:
            headCopy = None
        while p is not None:
            copy = p.__next__
            p.next = copy.__next__
            p = p.__next__
            if p is not None:
                copy.next = p.__next__
        return headCopy