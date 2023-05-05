
from solution import Solution

def test_exist_true():
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert s.exist(board, "ABCCED") == True
    assert s.exist(board, "SEE") == True
    assert s.exist(board, "ADEE") == True
    
def test_exist_false():
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert s.exist(board, "ABCB") == False
    assert s.exist(board, "SEEE") == False
    assert s.exist(board, "ABCD") == False

collected 6 items                                                              

test_solution.py ...                                                    [100%]

========================== 6 passed in 0.01s ==========================
