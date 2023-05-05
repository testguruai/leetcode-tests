import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_subdomainVisits(solution):
    assert solution.subdomainVisits(["9001 discuss.leetcode.com"]) == ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    assert solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]) == ["951 com", "900 google.mail.com", "1 intel.mail.com", "5 wiki.org", "50 yahoo.com"]