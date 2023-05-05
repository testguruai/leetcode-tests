import pytest

from solution import Solution

class TestSolution:
    
    def test_upsideDownBinaryTree_emptyTree(self):
        solution = Solution()
        assert solution.upsideDownBinaryTree(None) == None
        
    def test_upsideDownBinaryTree_singleNode(self):
        solution = Solution()
        root = TreeNode(1)
        assert solution.upsideDownBinaryTree(root).val == 1
        
    def test_upsideDownBinaryTree_twoNodes(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        assert solution.upsideDownBinaryTree(root).val == 2
        
    def test_upsideDownBinaryTree_threeNodes(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        assert solution.upsideDownBinaryTree(root).left.val == 3
        assert solution.upsideDownBinaryTree(root).right.val == 1
        assert solution.upsideDownBinaryTree(root).right.left.val == 2
        
    def test_upsideDownBinaryTree_balanced(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        assert solution.upsideDownBinaryTree(root).left.left.val == 7
        assert solution.upsideDownBinaryTree(root).left.right.val == 6
        assert solution.upsideDownBinaryTree(root).right.left.val == 5
        assert solution.upsideDownBinaryTree(root).right.right.val == 4
        
    def test_upsideDownBinaryTree_unbalanced(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        assert solution.upsideDownBinaryTree(root).left.left.val == 1
        assert solution.upsideDownBinaryTree(root).left.right.val == 4
        assert solution.upsideDownBinaryTree(root).right.left.val == 3
        assert solution.upsideDownBinaryTree(root).right.right.val == 2