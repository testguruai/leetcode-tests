
import pytest
from solution import Solution


def test_minMoves_when_empty_list_is_passed_then_returns_zero():
    assert Solution().minMoves([]) == 0


def test_minMoves_when_list_has_only_one_element_then_returns_zero():
    assert Solution().minMoves([0]) == 0


def test_minMoves_when_all_elements_of_list_are_same_then_returns_zero():
    assert Solution().minMoves([5, 5, 5]) == 0


def test_minMoves_when_list_has_both_positive_and_negative_integers_then_returns_correct_number_of_moves():
    assert Solution().minMoves([-10, 0, 10]) == 20


def test_minMoves_when_list_has_all_negative_integers_then_returns_correct_number_of_moves():
    assert Solution().minMoves([-3, -2, -1]) == 3


def test_minMoves_when_list_has_all_positive_integers_then_returns_correct_number_of_moves():
    assert Solution().minMoves([4, 5, 6]) == 3
