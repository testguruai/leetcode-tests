import pytest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def to_list(self):
        node_list = []
        node = self
        while node:
            node_list.append(node.val)
            node = node.next
        return node_list

class TestSolution:
    
    def test_oddEvenList_empty(self):
        sol = Solution()
        assert sol.oddEvenList(None) == None
    
    def test_oddEvenList_single(self):
        sol = Solution()
        node1 = ListNode(1)
        assert sol.oddEvenList(node1) == node1
    
    def test_oddEvenList_double(self):
        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        assert sol.oddEvenList(node1).to_list() == [1, 2]
    
    def test_oddEvenList_odd(self):
        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        assert sol.oddEvenList(node1).to_list() == [1, 3, 5, 2, 4]
    
    def test_oddEvenList_even(self):
        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        assert sol.oddEvenList(node1).to_list() == [1, 3, 2, 4]