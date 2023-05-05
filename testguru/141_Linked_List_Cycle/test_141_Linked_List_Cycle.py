import pytest

# from ListNode class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# from Solution class
class Solution:
    def hasCycle(self, head):
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next

            return True
        except:
            return False

def test_empty_list():
    s = Solution()
    assert s.hasCycle(None) == False

def test_single_node_no_cycle():
    s = Solution()
    node1 = ListNode(1)
    assert s.hasCycle(node1) == False

def test_two_nodes_no_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert s.hasCycle(node1) == False

def test_three_nodes_no_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    assert s.hasCycle(node1) == False

def test_three_nodes_with_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert s.hasCycle(node1) == True

def test_four_nodes_no_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    assert s.hasCycle(node1) == False

def test_four_nodes_with_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert s.hasCycle(node1) == True

def test_five_nodes_no_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    assert s.hasCycle(node1) == False

def test_five_nodes_with_cycle():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    assert s.hasCycle(node1) == True

def test_ten_nodes_no_cycle():
    s = Solution()
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    assert s.hasCycle(node0) == False

def test_ten_nodes_with_cycle():
    s = Solution()
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node4
    assert s.hasCycle(node0) == True