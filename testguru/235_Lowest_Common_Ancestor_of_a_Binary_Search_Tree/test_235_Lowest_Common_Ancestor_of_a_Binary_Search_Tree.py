#Pytest test cases for the given code.

#Test case1
def test_lowestCommonAncestor1():
    root=TreeNode(6)
    root.left=TreeNode(2)
    root.left.left=TreeNode(0)
    root.left.right=TreeNode(4)
    root.left.right.left=TreeNode(3)
    root.left.right.right=TreeNode(5)

    root.right=TreeNode(8)
    root.right.left=TreeNode(7)
    root.right.right=TreeNode(9)

    p=TreeNode(2)
    q=TreeNode(8)
    expected_ans=TreeNode(6)
    s=Solution()
    assert s.lowestCommonAncestor(root,p,q).val==expected_ans.val
    
#Test case2
def test_lowestCommonAncestor2():
    root=TreeNode(6)
    root.left=TreeNode(2)
    root.left.left=TreeNode(0)
    root.left.right=TreeNode(4)
    root.left.right.left=TreeNode(3)
    root.left.right.right=TreeNode(5)

    root.right=TreeNode(8)
    root.right.left=TreeNode(7)
    root.right.right=TreeNode(9)

    p=TreeNode(2)
    q=TreeNode(4)
    expected_ans=TreeNode(2)
    s=Solution()
    assert s.lowestCommonAncestor(root,p,q).val==expected_ans.val

#Test case3
def test_lowestCommonAncestor3():
    root=TreeNode(6)
    root.left=TreeNode(2)
    root.left.left=TreeNode(0)
    root.left.right=TreeNode(4)
    root.left.right.left=TreeNode(3)
    root.left.right.right=TreeNode(5)

    root.right=TreeNode(8)
    root.right.left=TreeNode(7)
    root.right.right=TreeNode(9)

    p=TreeNode(5)
    q=TreeNode(9)
    expected_ans=TreeNode(6)
    s=Solution()
    assert s.lowestCommonAncestor(root,p,q).val==expected_ans.val

#Test case4
def test_lowestCommonAncestor4():
    root=TreeNode(6)
    root.left=TreeNode(2)
    root.left.left=TreeNode(0)
    root.left.right=TreeNode(4)
    root.left.right.left=TreeNode(3)
    root.left.right.right=TreeNode(5)

    root.right=TreeNode(8)
    root.right.left=TreeNode(7)
    root.right.right=TreeNode(9)

    p=TreeNode(11)
    q=TreeNode(12)
    expected_ans=None
    s=Solution()
    assert s.lowestCommonAncestor(root,p,q)==expected_ans

#Test case5
def test_lowestCommonAncestor5():
    root=None
    p=None
    q=None
    expected_ans=None
    s=Solution()
    assert s.lowestCommonAncestor(root,p,q)==expected_ans