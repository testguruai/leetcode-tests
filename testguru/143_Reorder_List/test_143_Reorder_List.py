import pytest

from solution import Solution, ListNode

def test_reorderList_with_empty_list():
    sol = Solution()
    assert sol.reorderList(ListNode(None)) == None
    
def test_reorderList_with_single_node_list():
    sol = Solution()
    node1 = ListNode(1)
    assert sol.reorderList(node1) == node1

def test_reorderList_with_two_node_list():
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert sol.reorderList(node1) == node1
        
def test_reorderList_with_odd_number_node_list():
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
    
    sol.reorderList(node1)
    
    assert node1.val == 1
    assert node1.next.val == 5
    assert node1.next.next.val == 2
    assert node1.next.next.next.val == 4
    assert node1.next.next.next.next.val == 3
    assert node1.next.next.next.next.next == None

def test_reorderList_with_even_number_node_list():
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    sol.reorderList(node1)
    
    assert node1.val == 1
    assert node1.next.val == 4
    assert node1.next.next.val == 2
    assert node1.next.next.next.val == 3
    assert node1.next.next.next.next == None
