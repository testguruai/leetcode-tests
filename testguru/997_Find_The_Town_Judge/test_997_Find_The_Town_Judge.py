import pytest
from typing import List
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_findJudge_1(solution):
    assert solution.findJudge(1, []) == 1

def test_findJudge_2(solution):
    assert solution.findJudge(2, [[1,2]]) == 2

def test_findJudge_3(solution):
    assert solution.findJudge(2, [[1,2], [2,1]]) == -1

def test_findJudge_4(solution):
    assert solution.findJudge(3, [[1,3], [2,3]]) == 3

def test_findJudge_5(solution):
    assert solution.findJudge(3, [[1,3],[2,3],[3,1]]) == -1

def test_findJudge_6(solution):
    assert solution.findJudge(3, [[1,2],[2,3]]) == -1

def test_findJudge_7(solution):
    assert solution.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3

def test_findJudge_8(solution):
    assert solution.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[3,4]]) == 4

def test_findJudge_9(solution):
    assert solution.findJudge(5, [[1,2],[2,3],[3,4],[4,5],[5,1]]) == -1

def test_findJudge_10(solution):
    assert solution.findJudge(5, [[1,3],[2,3],[3,4],[4,5],[5,3]]) == 3