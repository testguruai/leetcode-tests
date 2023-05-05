import pytest

from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_defangIPaddr_replacing_dots_with_square_brackets(solution):
    assert solution.defangIPaddr("192.0.2.1") == "192[.]0[.]2[.]1"
    assert solution.defangIPaddr("10.0.0.1") == "10[.]0[.]0[.]1"

def test_defangIPaddr_joins_dots_with_square_brackets(solution):
    # assert solution.defangIPaddr("192.0.2.1") == "192[.]0[.]2[.]1"
    assert solution.defangIPaddr("127.0.0.1") == "127[.]0[.]0[.]1"

def test_defangIPaddr_using_regular_expression(solution):
    assert solution.defangIPaddr("192.0.2.1") == "192[.]0[.]2[.]1"
    assert solution.defangIPaddr("8.8.8.8") == "8[.]8[.]8[.]8"

def using_list_comprehension_join_characters(solution):
    assert solution.defangIPaddr("192.0.2.1") == "192[.]0[.]2[.]1"
    assert solution.defangIPaddr("255.255.255.0") == "255[.]255[.]255[.]0"