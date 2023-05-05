#test cases
def test_deleteDuplicates():
    #case1: head is None
    assert Solution().deleteDuplicates(None) == None
    
    #case2: no duplicates
    #(1)->(2)->(3)->(4)->(None)
    node4 = ListNode(4)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    
    node3.next = node4
    node2.next = node3
    node1.next = node2
    
    assert Solution().deleteDuplicates(node1) == node1
    
    #case3: duplicates at the beginning
    #(2)->(2)->(3)->(4)->(5)->(None)
    node5 = ListNode(5)
    node4 = ListNode(4)
    node3 = ListNode(3)
    node2_1 = ListNode(2)
    node2_2 = ListNode(2)
    
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2_2.next = node3
    node2_1.next = node2_2
    
    expected = node3
    expected.next = node4
    expected.next.next = node5
    
    assert Solution().deleteDuplicates(node2_1) == expected
    
    #case4: duplicates at the end
    #(1)->(2)->(3)->(4)->(4)->(None)
    node4_1 = ListNode(4)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    
    node4_1.next = None
    node3.next = node4_1
    node2.next = node3
    node1.next = node2
    
    expected = node1
    expected.next = node2
    expected.next.next = node3
    expected.next.next.next = node4_1
    
    assert Solution().deleteDuplicates(node1) == expected
    
    #case5: duplicates in middle and end
    #(1)->(2)->(2)->(3)->(4)->(4)->(None)
    node4_1 = ListNode(4)
    node4_2 = ListNode(4)
    node3 = ListNode(3)
    node2_1 = ListNode(2)
    node2_2 = ListNode(2)
    node1 = ListNode(1)
    
    node4_2.next = None
    node4_1.next = node4_2
    node3.next = node4_1
    node2_2.next = node3
    node2_1.next = node2_2
    node1.next = node2_1
    
    expected = node1
    expected.next = node3
    
    assert Solution().deleteDuplicates(node1) == expected
    
test_deleteDuplicates()