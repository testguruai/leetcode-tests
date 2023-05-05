import pytest

# Import the TreeNode class to use in tests
from solution import TreeNode

# Import the solution function
from solution import Solution

# Create an instance of the Solution class to use in tests
solution = Solution()

# Create test cases

def test_isSubtree():
    # Test case 1: s and t are both None
    assert solution.isSubtree(None, None) == True
    
    # Test case 2: s is None and t is not None
    s = None
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    assert solution.isSubtree(s, t) == False
    
    # Test case 3: s and t have different structures
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(4)
    assert solution.isSubtree(s, t) == False
    
    # Test case 4: s and t have the same structure and values
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    assert solution.isSubtree(s, t) == True
    
    # Test case 5: s and t have the same structure but different values
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(4)
    assert solution.isSubtree(s, t) == False
    
    # Test case 6: t is a subtree of s
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    assert solution.isSubtree(s, t) == True
    
    # Test case 7: t is not a subtree of s
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    assert solution.isSubtree(s, t) == False
    
    # Test case 8: t is the root of s
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    assert solution.isSubtree(t, t) == True
    
    # Test case 9: t is a leaf in s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    assert solution.isSubtree(s, s.left) == True
    
    # Test case 10: t is a leaf not in s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = TreeNode(4)
    assert solution.isSubtree(s, t) == False
    
    # Test case 11: t is the left subtree of s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = s.left
    assert solution.isSubtree(s, t) == True
    
    # Test case 12: t is the right subtree of s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = s.right
    assert solution.isSubtree(s, t) == True
    
    # Test case 13: t is a subtree of the left subtree of s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.left.left = TreeNode(4)
    s.left.right = TreeNode(5)
    s.right = TreeNode(3)
    t = s.left.right
    assert solution.isSubtree(s, t) == True
    
    # Test case 14: t is a subtree of the right subtree of s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    s.right.left = TreeNode(4)
    s.right.right = TreeNode(5)
    t = s.right.left
    assert solution.isSubtree(s, t) == True
    
    # Test case 15: t is not a subtree of any subtree of s
    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    s.right.left = TreeNode(4)
    s.right.right = TreeNode(5)
    t = TreeNode(6)
    assert solution.isSubtree(s, t) == False

# test_isSubtree()
