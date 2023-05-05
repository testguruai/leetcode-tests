import pytest

from solution import Solution

def test_solution():
    words1 = ["gin", "zen", "gig", "msg"]
    expected_output1 = 2
    solution = Solution()
    assert solution.uniqueMorseRepresentations(words1) == expected_output1

    words2 = []
    expected_output2 = 0
    assert solution.uniqueMorseRepresentations(words2) == expected_output2

    words3 = ["foo", "bar"]
    expected_output3 = 2
    assert solution.uniqueMorseRepresentations(words3) == expected_output3

    words4 = ["bad", "dad"]
    expected_output4 = 1
    assert solution.uniqueMorseRepresentations(words4) == expected_output4

    words5 = ["hello", "world"]
    expected_output5 = 2
    assert solution.uniqueMorseRepresentations(words5) == expected_output5

    words6 = ["sos", "eee"]
    expected_output6 = 2
    assert solution.uniqueMorseRepresentations(words6) == expected_output6

    words7 = ["aaa"]
    expected_output7 = 1
    assert solution.uniqueMorseRepresentations(words7) == expected_output7

    words8 = ["", "", ""]
    expected_output8 = 1
    assert solution.uniqueMorseRepresentations(words8) == expected_output8
