import pytest

def test_removeNthFromEnd_empty_list():
  s = Solution()
  assert s.removeNthFromEnd(None, 4) == None
  
def test_removeNthFromEnd_invalid_n():
  s = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  assert s.removeNthFromEnd(head, 7) == head
  
def test_removeNthFromEnd_remove_head():
  s = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  expected = head.next
  assert s.removeNthFromEnd(head, 5) == expected
  
def test_removeNthFromEnd_remove_tail():
  s = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  expected = ListNode(1)
  expected.next = ListNode(2)
  expected.next.next = ListNode(3)
  expected.next.next.next = ListNode(4)
  assert s.removeNthFromEnd(head, 1) == expected
  
def test_removeNthFromEnd_remove_middle():
  s = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  expected = ListNode(1)
  expected.next = ListNode(2)
  expected.next.next = ListNode(4)
  expected.next.next.next = ListNode(5)
  assert s.removeNthFromEnd(head, 2) == expected