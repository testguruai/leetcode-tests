import pytest

from solution import ListNode, Solution

def get_linked_list(lst):
    head = ListNode(lst[0])
    curr = head
    
    for i in range(1, len(lst)):
        node = ListNode(lst[i])
        curr.next = node
        curr = node
    
    return head

def linked_list_to_list(head):
    node = head
    lst = []
    
    while node:
        lst.append(node.val)
        node = node.next
    
    return lst

def test_deleteNode():
    sol = Solution()
    
    # Test case 1
    lst = [1, 2, 3, 4, 5]
    node_to_delete = get_linked_list(lst).next.next
    sol.deleteNode(node_to_delete)
    expected = [1, 2, 4, 5]
    assert linked_list_to_list(get_linked_list(lst)) == expected
    
    # Test case 2
    lst = [1, 2, 3, 4, 5]
    node_to_delete = get_linked_list(lst)
    sol.deleteNode(node_to_delete)
    expected = [2, 3, 4, 5]
    assert linked_list_to_list(get_linked_list(lst)) == expected
    
    # Test case 3
    lst = [1]
    node_to_delete = get_linked_list(lst)
    sol.deleteNode(node_to_delete)
    expected = []
    assert linked_list_to_list(get_linked_list(lst)) == expected
    
    # Test case 4
    lst = [1, 2, 3, 4, 5]
    node_to_delete = get_linked_list(lst).next.next.next.next
    sol.deleteNode(node_to_delete)
    expected = [1, 2, 3, 4]
    assert linked_list_to_list(get_linked_list(lst)) == expected