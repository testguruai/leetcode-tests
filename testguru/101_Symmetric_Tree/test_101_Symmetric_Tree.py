# Test cases for Solution class

def test_isSymmetric():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(2)
    node_4 = TreeNode(3)
    node_5 = TreeNode(4)
    node_6 = TreeNode(4)
    node_7 = TreeNode(3)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7
    solution = Solution()
    assert solution.isSymmetric(node_1) == True

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(2)
    node_4 = TreeNode(3)
    node_5 = TreeNode(3)
    node_1.left = node_2
    node_1.right = node_3
    node_2.right = node_4
    node_3.right = node_5
    solution = Solution()
    assert solution.isSymmetric(node_1) == False

    node_1 = TreeNode(2)
    node_2 = TreeNode(3)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(5)
    node_7 = TreeNode(4)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(9)
    node_11 = TreeNode(8)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7
    node_4.left = node_8
    node_4.right = node_9
    node_7.left = node_10
    node_7.right = node_11
    solution = Solution()
    assert solution.isSymmetric(node_1) == True

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(3)
    node_5 = TreeNode(2)
    node_1.left = node_2
    node_2.right = node_3
    node_1.right = node_4
    node_4.left = node_5
    solution = Solution()
    assert solution.isSymmetric(node_1) == False

    node_1 = None
    solution = Solution()
    assert solution.isSymmetric(node_1) == True