import heapq
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_kClosest_with_sorted_points(solution):
    points = [[1, 3], [-2, 2]]
    K = 1
    expected_output = [[-2, 2]]
    assert solution.kClosest(points, K) == expected_output

def test_kClosest_with_unsorted_points(solution):
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    expected_output = [[3, 3], [-2, 4]]
    assert solution.kClosest(points, K) == expected_output

def test_kClosest_with_points_on_origin(solution):
    points = [[0, 0], [1, 1], [-1, -1]]
    K = 2
    expected_output = [[0, 0], [1, 1]]
    assert solution.kClosest(points, K) == expected_output

def test_kClosest_with_K_larger_than_points(solution):
    points = [[2, 2], [3, 3], [4, 4]]
    K = 5
    expected_output = [[2, 2], [3, 3], [4, 4]]
    assert solution.kClosest(points, K) == expected_output