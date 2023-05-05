import pytest

def test_maximalSquare_bruteForce():
    sol = Solution()
    matrix1 = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    assert sol.maximalSquare(matrix1) == 4
    matrix2 = [['0', '1'], 
               ['1', '0']]
    assert sol.maximalSquare(matrix2) == 1
    matrix3 = [['0', '0', '0', '0'],
              ['1', '1', '1', '1'],
              ['0', '1', '1', '1'],
              ['0', '1', '0', '0']]
    assert sol.maximalSquare(matrix3) == 4


def test_maximalSquare_dp():
    sol = Solution()
    matrix1 = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    assert sol.maximalSquare(matrix1) == 4
    matrix2 = [['0', '1'], 
               ['1', '0']]
    assert sol.maximalSquare(matrix2) == 1
    matrix3 = [['0', '0', '0', '0'],
              ['1', '1', '1', '1'],
              ['0', '1', '1', '1'],
              ['0', '1', '0', '0']]
    assert sol.maximalSquare(matrix3) == 4


def test_maximalSquare_dp_nSpace():
    sol = Solution()
    matrix1 = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    assert sol.maximalSquare(matrix1) == 4
    matrix2 = [['0', '1'], 
               ['1', '0']]
    assert sol.maximalSquare(matrix2) == 1
    matrix3 = [['0', '0', '0', '0'],
              ['1', '1', '1', '1'],
              ['0', '1', '1', '1'],
              ['0', '1', '0', '0']]
    assert sol.maximalSquare(matrix3) == 4