import pytest
from solution import ListNode, Solution

# Sample Input
# 1 -> 2 -> 3 -> 4 -> 5 -> Null
# Expected Output
# Middle Node: 3

def test_middleNode():
    node5 = ListNode(5)
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2

    assert Solution().middleNode(node1) == node3

def test_middleNode_with_one_node():
    node1 = ListNode(1)

    assert Solution().middleNode(node1) == node1

def test_middleNode_with_two_node():
    node2 = ListNode(2)
    node1 = ListNode(1)
    node1.next = node2

    assert Solution().middleNode(node1) == node2

def test_middleNode_with_even_length():
    node6 = ListNode(6)
    node5 = ListNode(5)
    node5.next = node6
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2

    assert Solution().middleNode(node1) == node4

def test_middleNode_with_odd_length():
    node7 = ListNode(7)
    node6 = ListNode(6)
    node6.next = node7
    node5 = ListNode(5)
    node5.next = node6
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2

    assert Solution().middleNode(node1) == node4

def test_middleNode_with_empty_head():
    assert Solution().middleNode(None) == None

def test_middleNode_with_one_node_empty_list():
    node1 = ListNode(1)
    node1.next = None

    assert Solution().middleNode(node1) == node1