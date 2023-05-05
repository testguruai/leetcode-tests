import itertools

def test_permute_using_itertools():
    s = Solution()
    nums = [1,2,3]
    result = s.permute(nums)
    assert result == list(itertools.permutations(nums))

def test_permute_using_DPS_with_swapping():
    s = Solution()
    nums = [1,2,3]
    result = s.permute(nums)
    expected_output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    assert result == expected_output

def test_permute_iterative_solution():
    s = Solution()
    nums = [1,2,3]
    result = s.permute(nums)
    expected_output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    assert result == expected_output