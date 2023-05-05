import pytest
from solution import Solution

def test_totalNQueens():
    s = Solution()
    assert s.totalNQueens(0) == 0
    assert s.totalNQueens(1) == 1
    assert s.totalNQueens(2) == 0
    assert s.totalNQueens(3) == 0
    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(5) == 10
    assert s.totalNQueens(6) == 4
    assert s.totalNQueens(7) == 40
    assert s.totalNQueens(8) == 92
    assert s.totalNQueens(9) == 352
    assert s.totalNQueens(10) == 724

if __name__ == '__main__':
    pytest.main()
