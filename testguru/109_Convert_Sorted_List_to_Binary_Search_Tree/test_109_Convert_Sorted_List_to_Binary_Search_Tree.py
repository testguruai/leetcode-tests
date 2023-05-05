import pytest

def test_Solution():
    s = Solution()

    # Test 1 - empty linked list
    assert s.sortedListToBST(None) == None

    # Test 2 - linked list with one node
    head = ListNode(10)
    assert s.sortedListToBST(head).val == 10

    # Test 3 - linked list with multiple nodes
    head = ListNode(-10)
    n1 = ListNode(-3)
    n2 = ListNode(0)
    n3 = ListNode(5)
    n4 = ListNode(9)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    assert s.sortedListToBST(head).val == 0

    # Test 4 - linked list with negative values
    head = ListNode(-5)
    n1 = ListNode(-4)
    n2 = ListNode(-3)
    n3 = ListNode(-2)
    n4 = ListNode(-1)
    n5 = ListNode(0)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    assert s.sortedListToBST(head).val == -2

    # Test 5 - linked list with only even values
    head = ListNode(2)
    n1 = ListNode(4)
    n2 = ListNode(6)
    n3 = ListNode(8)
    n4 = ListNode(10)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    assert s.sortedListToBST(head).val == 6

    # Test 6 - linked list with only odd values
    head = ListNode(3)
    n1 = ListNode(5)
    n2 = ListNode(7)
    n3 = ListNode(9)
    n4 = ListNode(11)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    assert s.sortedListToBST(head).val == 7

    # Test 7 - linked list with repeating values
    head = ListNode(2)
    n1 = ListNode(2)
    n2 = ListNode(5)
    n3 = ListNode(5)
    n4 = ListNode(7)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    assert s.sortedListToBST(head).val == 5