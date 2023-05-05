import pytest
from solution import Solution, ListNode

def test_empty_list():
    s = Solution()
    assert s.partition(None, 5) == None

def test_single_node_list():
    s = Solution()
    head = ListNode(5)
    assert s.partition(head, 3) == head

def test_list_with_values_less_than_x():
    s = Solution()
    head = ListNode(2)
    temp = head
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(1)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(0)
    temp = temp.next
    res = s.partition(head, 5)
    while res is not None:
        assert res.val < 5
        res = res.next

def test_list_with_values_equal_to_or_greater_than_x():
    s = Solution()
    head = ListNode(2)
    temp = head
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(1)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(0)
    temp = temp.next
    res = s.partition(head, 5)
    while res is not None:
        assert res.val >= 5
        res = res.next

def test_list_with_values_before_and_after_x():
    s = Solution()
    head = ListNode(2)
    temp = head
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(1)
    temp = temp.next
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(0)
    temp = temp.next
    res = s.partition(head, 5)
    res_before = res_less = None
    res_after = res_greater = None
    while res is not None:
        if res.val < 5:
            if res_less is None:
                res_before = res_less = res
            else:
                res_less.next = res
                res_less = res_less.next
        else:
            if res_greater is None:
                res_after = res_greater = res
            else:
                res_greater.next = res
                res_greater = res_greater.next
        res = res.next
    res_less.next = res_after
    res = res_before
    while res is not None:
        assert res.val < 5 or res.val == 5
        res = res.next
    res = res_after
    while res is not None:
        assert res.val >= 5
        res = res.next
