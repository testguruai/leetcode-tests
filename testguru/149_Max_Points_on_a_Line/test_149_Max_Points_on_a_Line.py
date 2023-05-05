import pytest
from solution import Solution, Point

@pytest.fixture()
def solution():
    return Solution()

def test_maxPoints_with_null_input(solution):
    assert solution.maxPoints(None) == 0

def test_maxPoints_with_empty_list(solution):
    assert solution.maxPoints([]) == 0

def test_maxPoints_with_only_one_point(solution):
    points = [Point(0,0)]
    assert solution.maxPoints(points) == 1

def test_maxPoints_with_two_points(solution):
    points = [Point(0,0), Point(1,1)]
    assert solution.maxPoints(points) == 2

def test_maxPoints_with_horizontal_line(solution):
    points = [Point(0,0), Point(1,0), Point(-1,0)]
    assert solution.maxPoints(points) == 3

def test_maxPoints_with_vertical_line(solution):
    points = [Point(0,0), Point(0,1), Point(0,-1)]
    assert solution.maxPoints(points) == 3

def test_maxPoints_with_diagonal_line(solution):
    points = [Point(0,0), Point(1,1), Point(2,2)]
    assert solution.maxPoints(points) == 3

def test_maxPoints_with_same_points(solution):
    points = [Point(0,0), Point(0,0), Point(0,0)]
    assert solution.maxPoints(points) == 3

def test_generateGCD():
    solution = Solution()
    assert solution.generateGCD(1,2) == 1
    assert solution.generateGCD(2,4) == 2
    assert solution.generateGCD(3,5) == 1
    assert solution.generateGCD(6,9) == 3
    assert solution.generateGCD(8,12) == 4