import pytest

@pytest.fixture
def solution():
    return Solution()

def test_letterCombinations_empty(solution):
    assert solution.letterCombinations('') == []

def test_letterCombinations_single_digit(solution):
    assert solution.letterCombinations('2') == ['a', 'b', 'c']
    assert solution.letterCombinations('5') == ['j', 'k', 'l']
    assert solution.letterCombinations('0') == [' ']

def test_letterCombinations_multiple_digits(solution):
    assert solution.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert solution.letterCombinations('789') == ['ptw', 'ptx', 'pty', 'ptz', 'puw', 'pux', 'puy', 'puz', 'pvw', 'pvx', 'pvy', 'pvz', 'qtw', 'qtx', 'qty', 'qtz', 'quw', 'qux', 'quy', 'quz', 'qvw', 'qvx', 'qvy', 'qvz', 'rtw', 'rtx', 'rty', 'rtz', 'ruw', 'rux', 'ruy', 'ruz', 'rvw', 'rvx', 'rvy', 'rvz', 'stw', 'stx', 'sty', 'stz', 'suw', 'sux', 'suy', 'suz', 'svw', 'svx', 'svy', 'svz']
    assert solution.letterCombinations('8670') == ['t mp', 'u mp', 'v mp', 't mq', 'u mq', 'v mq', 't mr', 'u mr', 'v mr', 't ms', 'u ms', 'v ms', 't np', 'u np', 'v np', 't nq', 'u nq', 'v nq', 't nr', 'u nr', 'v nr', 't ns', 'u ns', 'v ns', 't op', 'u op', 'v op', 't oq', 'u oq', 'v oq', 't or', 'u or', 'v or', 't os', 'u os', 'v os']