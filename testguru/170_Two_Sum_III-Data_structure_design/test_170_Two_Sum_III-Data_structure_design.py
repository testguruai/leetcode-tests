import pytest

def test_add():
    ts = TwoSum()
    ts.add(1)
    ts.add(2)
    ts.add(3)
    assert ts.internal == [1, 2, 3]
    assert ts.dic == {1: False, 2: False, 3: False}

def test_find_true():
    ts = TwoSum()
    ts.add(1)
    ts.add(2)
    ts.add(3)
    assert ts.find(5) == True
    assert ts.find(3) == True

def test_find_false():
    ts = TwoSum()
    ts.add(1)
    ts.add(2)
    ts.add(3)
    assert ts.find(2) == False
    assert ts.find(6) == False