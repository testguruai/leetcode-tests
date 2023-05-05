import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_findSubstring(solution):
    assert solution.findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]