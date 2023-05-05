import pytest
from solution import Solution

def test_generate_possible_next_moves():
    solution = Solution()

    s1 = "++"
    actual_output1 = solution.generatePossibleNextMoves(s1)
    expected_output1 = ["--"]
    assert actual_output1 == expected_output1

    s2 = "+-+-"
    actual_output2 = solution.generatePossibleNextMoves(s2)
    expected_output2 = []
    assert actual_output2 == expected_output2

    s3 = ""
    actual_output3 = solution.generatePossibleNextMoves(s3)
    expected_output3 = []
    assert actual_output3 == expected_output3

    s4 = "++++"
    actual_output4 = solution.generatePossibleNextMoves(s4)
    expected_output4 = ["--++", "+--+" ,"++--"]
    assert actual_output4 == expected_output4

    s5 = "++-+"
    actual_output5 = solution.generatePossibleNextMoves(s5)
    expected_output5 = ["--+", "+--"]
    assert actual_output5 == expected_output5

    s6 = None
    actual_output6 = solution.generatePossibleNextMoves(s6)
    expected_output6 = []
    assert actual_output6 == expected_output6
