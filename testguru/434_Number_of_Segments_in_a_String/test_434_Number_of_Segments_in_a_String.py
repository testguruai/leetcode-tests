import pytest
from solution import Solution

def test_countSegments():
    sol = Solution()

    assert sol.countSegments("Hello, world!") == 2
    assert sol.countSegments("  Hello,  world! ") == 2
    assert sol.countSegments("   ") == 0
    assert sol.countSegments("") == 0
    assert sol.countSegments("a") == 1
    assert sol.countSegments("a b c") == 3
    assert sol.countSegments("a b   c   d") == 4
            
    # test edge cases
    assert sol.countSegments(None) == 0

    
    with pytest.raises(TypeError):
        sol.countSegments(123) # input not string type
        
        sol.countSegments(["a b c"]) # input not string type
        
pytest.main(["-v", "--tb=line", "-rN", "test_solution.py"])