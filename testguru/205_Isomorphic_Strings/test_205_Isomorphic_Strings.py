import pytest
from solution import Solution

def test_isIsomorphic():
    solution = Solution()
    s1 = "egg"
    t1 = "add"
    s2 = "foo"
    t2 = "bar"
    s3 = "paper"
    t3 = "title"
    s4 = ""
    t4 = ""
    s5 = "abcd"
    t5 = "efgh"
    s6 = "abc"
    t6 = "aaa"
    assert solution.isIsomorphic(s1, t1) == True
    assert solution.isIsomorphic(s2, t2) == False
    assert solution.isIsomorphic(s3, t3) == True
    assert solution.isIsomorphic(s4, t4) == True
    assert solution.isIsomorphic(s5, t5) == True
    assert solution.isIsomorphic(s6, t6) == False

# Additional tests for edge cases
def test_isIsomorphic_edge_cases():
    solution = Solution()
    s1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    s2 = "abababababababababababababababababab"
    t2 = "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
    s3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    t3 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert solution.isIsomorphic(s1, t1) == True
    assert solution.isIsomorphic(s2, t2) == True
    assert solution.isIsomorphic(s3, t3) == True
