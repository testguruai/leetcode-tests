import pytest
from solution import Solution

def test_solve():
    s = Solution()
    
    # Test empty board
    board = []
    s.solve(board)
    assert board == []
    
    # Test board with no "O"s
    board = [["X","X","X"],
             ["X","X","X"],
             ["X","X","X"]]
    s.solve(board)
    assert board == [["X","X","X"],
                     ["X","X","X"],
                     ["X","X","X"]]
    
    # Test board with "O"s on the borders
    board = [["X","O","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    s.solve(board)
    assert board == [["X","O","X","X"],
                     ["X","O","O","X"],
                     ["X","X","O","X"],
                     ["X","O","X","X"]]

    # Test board with "O"s not surrounded by "X"s
    board = [["X","O","X","X"],
             ["X","O","O","X"],
             ["X","X","X","X"],
             ["X","O","X","X"]]
    s.solve(board)
    assert board == [["X","O","X","X"],
                     ["X","O","O","X"],
                     ["X","X","X","X"],
                     ["X","O","X","X"]]