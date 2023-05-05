import pytest

from solution import Solution

def test_groupAnagrams():
    s = Solution()
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
    actual_output = s.groupAnagrams(input_list)
    assert len(actual_output) == len(expected_output)
    for lst in actual_output:
        assert lst in expected_output
    
    input_list = ["a"]
    expected_output = [["a"]]
    actual_output = s.groupAnagrams(input_list)
    assert actual_output == expected_output

    input_list = [""]
    expected_output = [[""]]
    actual_output = s.groupAnagrams(input_list)
    assert actual_output == expected_output

    input_list = []
    expected_output = []
    actual_output = s.groupAnagrams(input_list)
    assert actual_output == expected_output

    input_list = ["eat"]
    expected_output = [["eat"]]
    actual_output = s.groupAnagrams(input_list)
    assert actual_output == expected_output