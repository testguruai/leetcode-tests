import pytest

from solution import Solution


def test_reorderLogFiles_with_only_digit_logs():
    s = Solution()
    logs = ["2 12 3", "1 23 4"]
    assert s.reorderLogFiles(logs) == ["2 12 3", "1 23 4"]


def test_reorderLogFiles_with_only_letter_logs():
    s = Solution()
    logs = ["a abcd", "b bcde", "c cdef"]
    assert s.reorderLogFiles(logs) == ["a abcd", "b bcde", "c cdef"]


def test_reorderLogFiles_with_mixed_logs():
    s = Solution()
    logs = ["a abcd", "b bcde", "c cdef", "2 12 3", "1 23 4"]
    assert s.reorderLogFiles(logs) == ["a abcd", "b bcde", "c cdef", "1 23 4", "2 12 3"]


def test_reorderLogFiles_with_letter_logs_with_same_content():
    s = Solution()
    logs = ["a abcd", "b bcde", "c cdef", "d bcde", "e abcd", "f cdef"]
    assert s.reorderLogFiles(logs) == ["a abcd", "e abcd", "b bcde", "d bcde", "c cdef", "f cdef"]


def test_reorderLogFiles_with_empty_logs():
    s = Solution()
    logs = []
    assert s.reorderLogFiles(logs) == []