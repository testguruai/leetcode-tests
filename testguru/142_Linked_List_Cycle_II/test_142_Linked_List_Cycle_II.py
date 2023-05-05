
import pytest

class TestSolution:
    def test_detectCycle(self):
      # creating LinkedList with cycle
      head = ListNode(1)
      node2 = ListNode(2)
      head.next = node2
      node3 = ListNode(3)
      node2.next = node3
      node4 = ListNode(4)
      node3.next = node4
      node5 = ListNode(5)
      node4.next = node5
      node5.next = node2

      obj = Solution()
      assert obj.detectCycle(head) == node2

    def test_detectCycle_no_cycle(self):
      # creating LinkedList without cycle
      head = ListNode(1)
      node2 = ListNode(2)
      head.next = node2
      node3 = ListNode(3)
      node2.next = node3
      node4 = ListNode(4)
      node3.next = node4

      obj = Solution()
      assert obj.detectCycle(head) == None

    def test_detectCycle_singleton(self):
      # creating LinkedList with only one node
      head = ListNode(1)

      obj = Solution()
      assert obj.detectCycle(head) == None

pytest test_solution.py
