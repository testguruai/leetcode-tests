import pytest

from solution import Solution

def test_countDaysTogether():
    solution = Solution()

    # Test Case 1
    arriveAlice = "2021-01-01"
    leaveAlice = "2021-01-03"
    arriveBob = "2021-01-02"
    leaveBob = "2021-01-04"
    expected_output = 2
    assert solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == expected_output

    # Test Case 2
    arriveAlice = "2021-01-01"
    leaveAlice = "2021-01-03"
    arriveBob = "2021-01-04"
    leaveBob = "2021-01-06"
    expected_output = 0
    assert solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == expected_output

    # Test Case 3
    arriveAlice = "2022-09-30"
    leaveAlice = "2022-10-01"
    arriveBob = "2022-10-01"
    leaveBob = "2022-10-02"
    expected_output = 1
    assert solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == expected_output

    # Test Case 4
    arriveAlice = "2021-12-31"
    leaveAlice = "2022-01-01"
    arriveBob = "2022-01-01"
    leaveBob = "2022-01-02"
    expected_output = 2
    assert solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == expected_output

    # Test Case 5
    arriveAlice = "2021-01-01"
    leaveAlice = "2021-12-31"
    arriveBob = "2022-01-01"
    leaveBob = "2022-12-31"
    expected_output = 0
    assert solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == expected_output

    # Test Case 6
    arriveAlice = "2022-03-14"
    leaveAlice = "2022-03-15"
    arriveBob = "2022-03-13"
    leaveBob = "2022-03-14"
    expected_output = 1
    assert solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == expected_output