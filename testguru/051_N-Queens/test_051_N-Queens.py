import pytest

@pytest.fixture
def setup():
    s = Solution()
    return s

def test_do_solveNQueens(setup):
    res = []
    board = [['.'] * 4 for t in range(4)]
    s.do_solveNQueens(res, board, 4)
    assert res == [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

def test_solveNQueens(setup):
    assert setup.solveNQueens(4) == [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]