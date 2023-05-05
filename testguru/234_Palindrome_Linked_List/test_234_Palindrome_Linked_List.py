import pytest

from solution import Solution, ListNode


def test_empty_list():
    assert Solution().isPalindrome(None) == True


def test_single_valued_list():
    node_1 = ListNode(1)
    assert Solution().isPalindrome(node_1) == True


def test_two_valued_list_different():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    assert Solution().isPalindrome(node_1) == False


def test_two_valued_list_same():
    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_1.next = node_2
    assert Solution().isPalindrome(node_1) == True


def test_three_valued_list_palindrome():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(1)
    node_1.next = node_2
    node_2.next = node_3
    assert Solution().isPalindrome(node_1) == True


def test_three_valued_list_not_palindrome():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_1.next = node_2
    node_2.next = node_3
    assert Solution().isPalindrome(node_1) == False


def test_four_valued_list_palindrome():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(2)
    node_4 = ListNode(1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    assert Solution().isPalindrome(node_1) == True


def test_four_valued_list_not_palindrome():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(2)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    assert Solution().isPalindrome(node_1) == False


def test_five_valued_list_palindrome():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(2)
    node_5 = ListNode(1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    assert Solution().isPalindrome(node_1) == True


def test_five_valued_list_not_palindrome():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    assert Solution().isPalindrome(node_1) == False
