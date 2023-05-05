import pytest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestSolution:
    def create_linked_list(self, lst):
        """
        Helper function to create a linked list
        given a list of values
        """
        head = ListNode(lst[0])
        curr = head
        for val in lst[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def linked_list_to_list(self, head):
        """
        Helper function to convert a linked list
        into a list of values
        """
        lst = []
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        return lst

    def test_reverseBetween(self):
        solution = Solution()
        
        # Test case 1
        head = self.create_linked_list([1,2,3,4,5])
        m = 2
        n = 4
        expected_output = [1,4,3,2,5]
        result = solution.reverseBetween(head, m, n)
        assert self.linked_list_to_list(result) == expected_output
        
        # Test case 2
        head = self.create_linked_list([1,2,3,4,5])
        m = 1
        n = 5
        expected_output = [5,4,3,2,1]
        result = solution.reverseBetween(head, m, n)
        assert self.linked_list_to_list(result) == expected_output
        
        # Test case 3
        head = self.create_linked_list([1])
        m = 1
        n = 1
        expected_output = [1]
        result = solution.reverseBetween(head, m, n)
        assert self.linked_list_to_list(result) == expected_output
        
        # Test case 4
        head = self.create_linked_list([1,2,3])
        m = 2
        n = 2
        expected_output = [1,2,3]
        result = solution.reverseBetween(head, m, n)
        assert self.linked_list_to_list(result) == expected_output
        
        # Test case 5
        head = self.create_linked_list([1,2,3,4,5])
        m = 2
        n = 6
        expected_output = [1,5,4,3,2]
        result = solution.reverseBetween(head, m, n)
        assert self.linked_list_to_list(result) == expected_output