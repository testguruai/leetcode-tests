import pytest

dictionary = ["hello", "world", "hi", "python"]
vwa = ValidWordAbbr(dictionary)

def test_abbre_for_hello():
    assert vwa.getAbb("hello") == "h3o"
    
def test_abbre_for_a():
    assert vwa.getAbb("a") == "a"
    
def test_abbre_for_hi():
    assert vwa.getAbb("hi") == "hi"
    
def test_isUnique_for_hello():
    assert vwa.isUnique("hello") == False
    
def test_isUnique_for_python():
    assert vwa.isUnique("python") == True
    
def test_isUnique_for_new():
    assert vwa.isUnique("new") == True
    
def test_isUnique_for_abc():
    assert vwa.isUnique("abc") == True