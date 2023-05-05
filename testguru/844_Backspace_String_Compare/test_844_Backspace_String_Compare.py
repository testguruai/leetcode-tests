import pytest

def test_backspaceCompare():
    obj = Solution()

    # Test 1
    s = "ab#c"
    t = "ad#c"
    assert obj.backspaceCompare(s, t) == True

    # Test 2
    s = "ab##"
    t = "c#d#"
    assert obj.backspaceCompare(s, t) == True

    # Test 3
    s = "a##c"
    t = "#a#c"
    assert obj.backspaceCompare(s, t) == True

    # Test 4
    s = "a#c"
    t = "b"
    assert obj.backspaceCompare(s, t) == False

    # Test 5
    s = ""
    t = ""
    assert obj.backspaceCompare(s, t) == True

    # Test 6
    s = "###"
    t = "##"
    assert obj.backspaceCompare(s, t) == True

    # Test 7
    s = "abc##d"
    t = "b#d"
    assert obj.backspaceCompare(s, t) == True

    # Test 8
    s = "abcd"
    t = "defg"
    assert obj.backspaceCompare(s, t) == False

    # Test 9
    s = "xy#z"
    t = "xzz#"
    assert obj.backspaceCompare(s, t) == False

    # Test 10
    s = "#z#z"
    t = "z#"
    assert obj.backspaceCompare(s, t) == True

    # Test 11
    s = "y#y#y#y#y#"
    t = "y#y#y#y#y#"
    assert obj.backspaceCompare(s, t) == False

    # Test 12
    s = "a"
    t = "b"
    assert obj.backspaceCompare(s, t) == False

    # Test 13
    s = "a"
    t = "a"
    assert obj.backspaceCompare(s, t) == True

    # Test 14
    s = "aaa###a"
    t = "ab#a###"
    assert obj.backspaceCompare(s, t) == True

    # Test 15
    s = "#"
    t = "a"
    assert obj.backspaceCompare(s, t) == False

    # Test 16
    s = ""
    t = "c"
    assert obj.backspaceCompare(s, t) == False

    # Test 17
    s = "b##c"
    t = "#a#c"
    assert obj.backspaceCompare(s, t) == True

    # Test 18
    s = "xy#z"
    t = "xyz##"
    assert obj.backspaceCompare(s, t) == True

    # Test 19
    s = "aaa###a"
    t = "ab###a"
    assert obj.backspaceCompare(s, t) == True

    # Test 20
    s = "b#"
    t = "a"
    assert obj.backspaceCompare(s, t) == False

    # Test 21
    s = "ab"
    t = "a#c#b"
    assert obj.backspaceCompare(s, t) == True

    # Test 22
    s = "qrs#y##y#t#h"
    t = "y##y#s#t#r###h"
    assert obj.backspaceCompare(s, t) == True

    # Test 23
    s = "ab#c"
    t = "ad#c"
    assert obj.backspaceCompare(s, t) == True

    # Test 24
    s = "ab##"
    t = "c#d#"
    assert obj.backspaceCompare(s, t) == True

    # Test 25
    s = "a##c"
    t = "#a#c"
    assert obj.backspaceCompare(s, t) == True

    # Test 26
    s = "a#c"
    t = "b"
    assert obj.backspaceCompare(s, t) == False

    # Test 27
    s = ""
    t = ""
    assert obj.backspaceCompare(s, t) == True

    # Test 28
    s = "abc##d"
    t = "b#d"
    assert obj.backspaceCompare(s, t) == True

    # Test 29
    s = "abcd"
    t = "defg"
    assert obj.backspaceCompare(s, t) == False

    # Test 30
    s = "xy#z"
    t = "xzz#"
    assert obj.backspaceCompare(s, t) == False

    # Test 31
    s = "#z#z"
    t = "z#"
    assert obj.backspaceCompare(s, t) == True

    # Test 32
    s = "y#y#y#y#y#"
    t = "y#y#y#y#y#"
    assert obj.backspaceCompare(s, t) == False

    # Test 33
    s = "a"
    t = "b"
    assert obj.backspaceCompare(s, t) == False

    # Test 34
    s = "a"
    t = "a"
    assert obj.backspaceCompare(s, t) == True

    # Test 35
    s = "aaa###a"
    t = "ab#a###"
    assert obj.backspaceCompare(s, t) == True

    # Test 36
    s = "#"
    t = "a"
    assert obj.backspaceCompare(s, t) == False

    # Test 37
    s = ""
    t = "c"
    assert obj.backspaceCompare(s, t) == False

    # Test 38
    s = "b##c"
    t = "#a#c"
    assert obj.backspaceCompare(s, t) == True

    # Test 39
    s = "xy#z"
    t = "xyz##"
    assert obj.backspaceCompare(s, t) == True

    # Test 40
    s = "aaa###a"
    t = "ab###a"
    assert obj.backspaceCompare(s, t) == True

    # Test 41
    s = "b#"
    t = "a"
    assert obj.backspaceCompare(s, t) == False

    # Test 42
    s = "ab"
    t = "a#c#b"
    assert obj.backspaceCompare(s, t) == True

    # Test 43
    s = "qrs#y##y#t#h"
    t = "y##y#s#t#r###h"
    assert obj.backspaceCompare(s, t) == True

    # Test 44
    s = "ab#cdef"
    t = "ab#c"
    assert obj.backspaceCompare(s, t) == False

    # Test 45
    s = "qwertyuiopasdfghjklzxcvbnm#"
    t = "qwertyuiopasdfghjklzxcvbnm#"
    assert obj.backspaceCompare(s, t) == True

    # Test 46
    s = "qwertyuiopasdfghjklzxcvbnm#"
    t = "qwertyuiopasdfghjklzxcvbnm"
    assert obj.backspaceCompare(s, t) == False

    # Test 47
    s = "qwertyuiopasdfghjkl#zx"
    t = "qwertyuiopasdfghjkl#zx"
    assert obj.backspaceCompare(s, t) == True

    # Test 48
    s = "qwertyuiopasdfghjkl#zx"
    t = "qwertyuiopasdfghjklzx"
    assert obj.backspaceCompare(s, t) == False

    # Test 49
    s = "qwertyuiopasdfghjkl#zx"
    t = ""
    assert obj.backspaceCompare(s, t) == False

    # Test 50
    s = "#"
    t = "#"
    assert obj.backspaceCompare(s, t) == True