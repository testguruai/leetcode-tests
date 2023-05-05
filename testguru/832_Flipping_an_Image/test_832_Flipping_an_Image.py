import pytest
from typing import List
from solution import Solution

solution = Solution()

def test_flipAndInvertImage_whenGivenEmptyList_returnsEmptyList():
    assert solution.flipAndInvertImage([]) == []

def test_flipAndInvertImage_whenGivenSingleEmptyList_returnsSingleEmptyList():
    assert solution.flipAndInvertImage([[]]) == [[]]

def test_flipAndInvertImage_whenGivenSingleListWithASingle0_returnsSingleListWithASingle1():
    assert solution.flipAndInvertImage([[0]]) == [[1]]

def test_flipAndInvertImage_whenGivenSingleListWithASingle1_returnsSingleListWithASingle0():
    assert solution.flipAndInvertImage([[1]]) == [[0]]

def test_flipAndInvertImage_whenGivenSingleListWithMultiple0s_returnsSingleListWithMultiple1s():
    assert solution.flipAndInvertImage([[0, 0, 0]]) == [[1, 1, 1]]

def test_flipAndInvertImage_whenGivenSingleListWithMultiple1s_returnsSingleListWithMultiple0s():
    assert solution.flipAndInvertImage([[1, 1, 1]]) == [[0, 0, 0]]

def test_flipAndInvertImage_whenGivenMultipleSingleLists_returnsMultipleSingleLists_InvertedAndReversed():
    assert solution.flipAndInvertImage([[0], [1]]) == [[1], [0]]
    assert solution.flipAndInvertImage([[1], [0]]) == [[0], [1]]
    
def test_flipAndInvertImage_whenGivenMultipleLists_returnsMultipleLists_InvertedAndReversed():
    assert solution.flipAndInvertImage([[0, 1], [1, 0]]) == [[1, 0], [0, 1]]
    assert solution.flipAndInvertImage([[1, 0], [0, 1]]) == [[0, 1], [1, 0]]

def test_flipAndInvertImage_whenGivenALargeList_returnsLargeList_InvertedAndReversed():
    assert solution.flipAndInvertImage([
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 0]
    ]) == [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0]
    ]

def test_flipAndInvertImage_whenGivenALargeList_returnsLargeList_InvertedAndReversed_AlternativeMethod():
    assert solution.flipAndInvertImage([
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 0]
    ]) == [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 0]
    ]