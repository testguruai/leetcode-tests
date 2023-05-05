import pytest
from solution import Solution

def test_findLadders():
    s = Solution()
    assert s.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"])) == [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    assert s.findLadders('a', 'b', set(['a', 'b', 'c'])) == [['a', 'b']]
    assert s.findLadders('hot', 'dog', set(['hot', 'dog'])) == []
    assert s.findLadders("qa", "sq", set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])) == ['qa', 'ba', 'be', 'se', 'sq']
    assert s.findLadders("hot", "dog", set(["hot","cog","dog","tot","hog","hop","pot","dot"])) == [['hot', 'dot', 'dog'] , ['hot', 'hog', 'cog', 'dog']]
    
    with pytest.raises(TypeError):
        s.findLadders(123, 'dog', set(['hot', 'dog'])) # Should raise TypeError when beginWord is integer

    with pytest.raises(TypeError):
        s.findLadders('dog', 123, set(['hot', 'dog'])) # Should raise TypeError when endWord is integer

    with pytest.raises(TypeError):
        s.findLadders('dog', 'cat', ['hot', 'dog']) # Should raise TypeError when wordlist is not a set

    assert s.findLadders('hit', 'cog', set([])) == [] # Empty wordlist
    
    assert s.findLadders('hit', 'cog', set(['hot'])) == [] # Only one element in wordList
    
    assert s.findLadders('hot', 'dog', set(['hot', 'cog'])) == [] # No possible path from beginWord to endWord

    assert s.findLadders("hit", "cog", set(["hot","dot","dog","lot","log","cog"])) == [['hit', 'hot', 'dot', 'dog', 'cog']] # Random test case with 6 words in wordlist