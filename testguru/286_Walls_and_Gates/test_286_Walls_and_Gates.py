import pytest

from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_wallsAndGates_empty_solution(solution):
    rooms = []
    solution.wallsAndGates(rooms)
    assert rooms == []

def test_wallsAndGates_single_gate(solution):
    rooms = [[2147483647, -1, 0, 2147483647],
             [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [0, -1, 2147483647, 2147483647]]

    solution.wallsAndGates(rooms)

    expected_rooms = [[3, -1, 0, 1],
                      [2, 2, 1, -1],
                      [1, -1, 2, -1],
                      [0, -1, 3, 4]]

    assert rooms == expected_rooms

def test_wallsAndGates_multiple_gates(solution):
    rooms = [[2147483647, -1, 0, 2147483647],
             [2147483647, -1, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [0, -1, 2147483647, 2147483647]]

    solution.wallsAndGates(rooms)

    expected_rooms = [[3, -1, 0, 1],
                      [2, -1, 1, -1],
                      [1, -1, 2, -1],
                      [0, -1, 3, 4]]

    assert rooms == expected_rooms

def test_wallsAndGates_no_gates(solution):
    rooms = [[2147483647, -1, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [2147483647, -1, 2147483647, 2147483647]]

    solution.wallsAndGates(rooms)

    expected_rooms = [[2147483647, -1, 2147483647, -1],
                      [2147483647, -1, 2147483647, -1],
                      [2147483647, -1, 2147483647, -1],
                      [2147483647, -1, 2147483647, 2147483647]]

    assert rooms == expected_rooms

def test_wallsAndGates_all_gates_at_same_position(solution):
    rooms = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    solution.wallsAndGates(rooms)

    expected_rooms = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

    assert rooms == expected_rooms

def test_wallsAndGates_all_walls(solution):
    rooms = [[-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1]]

    solution.wallsAndGates(rooms)

    expected_rooms = [[-1, -1, -1, -1],
                      [-1, -1, -1, -1],
                      [-1, -1, -1, -1],
                      [-1, -1, -1, -1]]

    assert rooms == expected_rooms