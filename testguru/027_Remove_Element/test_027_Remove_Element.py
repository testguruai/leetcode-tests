import pytest

def test_empty_list():
    s = Solution()
    assert s.removeElement([], 1) == 0

def test_remove_all_elements():
    s = Solution()
    assert s.removeElement([1, 1, 1, 1], 1) == 0

def test_remove_no_elements():
    s = Solution()
    assert s.removeElement([1, 2, 3], 4) == 3

def test_remove_some_elements():
    s = Solution()
    assert s.removeElement([1, 2, 3, 4, 3], 3) == 3

def test_remove_just_one_element():
    s = Solution()
    assert s.removeElement([1, 2, 3, 4, 3], 4) == 4

def test_remove_with_multiple_occurrences():
    s = Solution()
    assert s.removeElement([1, 2, 3, 1, 2, 3, 1, 2, 3], 3) == 6