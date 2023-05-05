import pytest
from random import randint

class TestSolution:
    def test_copyRandomList_none(self):
        solution = Solution()
        result = solution.copyRandomList(None) # should return None
        assert result == None

    def test_copyRandomList(self):
        solution = Solution()
        original_list = RandomListNode(1)
        original_list.next = RandomListNode(2)
        original_list.next.next = RandomListNode(3)
        original_list.next.next.next  = RandomListNode(4)
        original_list.next.next.next.next = RandomListNode(5)
        original_list.random = original_list.next.next
        original_list.next.random = original_list.next.next.next
        original_list.next.next.random = original_list.next.next.next.next
        original_list.next.next.next.random = original_list.next
        original_list.next.next.next.next.random = original_list.next.next.next.next
        result = solution.copyRandomList(original_list)

        #original list should not be modified
        assert original_list == original_list 

        #length of original and copy list should be same
        assert self.length(original_list) == self.length(result)

        #test if all elements from the original list exists in the copy list
        while original_list:
            assert original_list.label == result.label
            if original_list.random:
                assert original_list.random.label == result.random.label
            else:
                assert original_list.random == result.random
            original_list = original_list.next
            result = result.next
            
    def length(self, node: RandomListNode):
        length = 0
        while node != None:
            length +=1
            node = node.next
        return length