
from solution import Solution

def test_toLowerCase1():
    s = Solution()
    assert s.toLowerCase("Hello World") == "hello world"
    
def test_toLowerCase2():
    s = Solution()
    assert s.toLowerCase("HELLO WORLD") == "hello world"

def test_toLowerCase3():
    s = Solution()
    assert s.toLowerCase("") == ""

def test_toLowerCase4():
    s = Solution()
    assert s.toLowerCase("aBCdE") == "abcde"
