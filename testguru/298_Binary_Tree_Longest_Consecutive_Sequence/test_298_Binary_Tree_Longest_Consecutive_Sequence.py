# Let's first define some test cases

def test_longestConsecutive():
    # Test case 1: Root is None
    assert Solution().longestConsecutive(None) == 0

    # Test case 2: Single node in the tree
    assert Solution().longestConsecutive(TreeNode(1)) == 1

    # Test case 3: All nodes are consecutive - Top down approach
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    assert Solution().longestConsecutive(root) == 3

    # Test case 4: All nodes are consecutive - Bottom up approach
    # (commenting out the top-down part of the code)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.right = TreeNode(6)
    # assert Solution().longestConsecutive(root) == 3

    # Test case 5: Non-continuous nodes present - Top down approach
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert Solution().longestConsecutive(root) == 3

    # Test case 6: Non-continuous nodes present - Bottom up approach
    # (commenting out the top-down part of the code)
    # root = TreeNode(2)
    # root.left = TreeNode(1)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(5)
    # assert Solution().longestConsecutive(root) == 3

    # Test case 7: Some nodes are consecutive, some are not - Top down approach
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    assert Solution().longestConsecutive(root) == 2

    # Test case 8: Some nodes are consecutive, some are not - Bottom up approach
    # (commenting out the top-down part of the code)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right.right = TreeNode(7)
    # assert Solution().longestConsecutive(root) == 2

    print("All test cases pass")

test_longestConsecutive()  # run the test function to check