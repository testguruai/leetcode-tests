import pytest

# Create test for the class Solution

# Test case 1: Test for valid inputs
def test_kWeakestRows_valid_inputs(Solution):
    assert Solution.kWeakestRows([[1,1,0,0,0],
                                  [1,1,1,1,0],
                                  [1,0,0,0,0]], 2) == [0, 2]

# Test case 2: Test for k larger than number of rows
def test_kWeakestRows_k_larger_than_rows(Solution):
    assert Solution.kWeakestRows([[1,1,0],[1,1,1],[1,0,0]], 5) == [0, 1, 2]

# Test case 3: Test for empty matrix
def test_kWeakestRows_empty_matrix(Solution):
    assert Solution.kWeakestRows([], 2) == []

# Test case 4: Test for k equal to zero
def test_kWeakestRows_k_equal_to_0(Solution):
    assert Solution.kWeakestRows([[1,1,0],[1,1,1],[1,0,0]], 0) == []

# Test case 5: Test for non integer k
def test_kWeakestRows_non_integer_k(Solution):
    with pytest.raises(TypeError):
        Solution.kWeakestRows([[1,1,0],[1,1,1],[1,0,0]], "two")