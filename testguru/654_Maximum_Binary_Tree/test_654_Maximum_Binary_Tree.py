import pytest


class TestSolution:
    def test_constructMaximumBinaryTree_emptyList(self):
        """
        Test that empty input list returns None
        """
        sol = Solution()
        assert sol.constructMaximumBinaryTree([]) == None

    def test_constructMaximumBinaryTree_singleElement(self):
        """
        Test that single element input list returns a TreeNode with that value
        """
        sol = Solution()
        root = sol.constructMaximumBinaryTree([5])
        assert root.val == 5
        assert root.left == None
        assert root.right == None

    def test_constructMaximumBinaryTree_multipleElements(self):
        """
        Test that input list with multiple elements returns a correctly constructed maximum binary tree
        """
        sol = Solution()
        root = sol.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
        assert root.val == 6
        assert root.left.val == 3
        assert root.left.left == None
        assert root.left.right.val == 2
        assert root.left.right.left == None
        assert root.left.right.right.val == 1
        assert root.right.val == 5
        assert root.right.left.val == 0
        assert root.right.right == None

    # def test_constructMaximumBinaryTree_alternateSolution(self):
    #     """
    #     Test that the alternate solution (using a stack) returns the same result as the first solution
    #     """
    #     sol = Solution()
    #     input_list = [3, 2, 1, 6, 0, 5]
    #     root1 = sol.constructMaximumBinaryTree(input_list)
    #     root2 = sol.constructMaximumBinaryTree(input_list)
    #     assert self.checkTreesEqual(root1, root2)

    # # Helper function to check if two trees are equal (not part of the class, so cannot use self)
    # def checkTreesEqual(tree1, tree2):
    #     if tree1 == None and tree2 == None:
    #         return True
    #     elif tree1 == None or tree2 == None:
    #         return False
    #     elif tree1.val != tree2.val:
    #         return False
    #     else:
    #         return checkTreesEqual(tree1.left, tree2.left) and checkTreesEqual(tree1.right, tree2.right)

# To run the tests, use pytest in the command line in the same directory as this file.