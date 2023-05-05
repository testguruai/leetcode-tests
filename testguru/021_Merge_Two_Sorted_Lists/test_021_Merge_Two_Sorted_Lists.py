import pytest

class TestMergeTwoLists(object):
    def test_mergeTwoLists(self):
        # Testcase 1: Both lists are empty
        solution = Solution()
        assert solution.mergeTwoLists(None, None) == None
        
        # Testcase 2: One list is empty and the other is non-empty
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l2 = None
        expected = l1
        assert solution.mergeTwoLists(l1, l2) == expected
        
        l1 = None
        l2 = ListNode(1)
        l2.next = ListNode(2)
        expected = l2
        assert solution.mergeTwoLists(l1, l2) == expected
        
        # Testcase 3: Lists have same length
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        expected.next.next.next.next = ListNode(4)
        expected.next.next.next.next.next = ListNode(4)
        assert solution.mergeTwoLists(l1, l2) == expected
        
        # Testcase 4: Lists have different length
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        expected.next.next.next.next = ListNode(4)
        assert solution.mergeTwoLists(l1, l2) == expected
        
        # Testcase 5: One of the lists is longer than the other
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        expected.next.next.next.next = ListNode(4)
        assert solution.mergeTwolists(l1, l2) == expected

if __name__ == '__main__':
    pytest.main()