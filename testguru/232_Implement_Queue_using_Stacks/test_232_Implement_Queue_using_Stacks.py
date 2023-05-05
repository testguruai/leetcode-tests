import pytest

def test_push():
    q = Queue()
    q.push(1)
    assert q.peek() == 1

def test_pop():
    q = Queue()
    q.push(1)
    q.push(2)
    q.pop()
    assert q.peek() == 2

def test_peek():
    q = Queue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1

def test_empty():
    q = Queue()
    assert q.empty() == True
    q.push(1)
    assert q.empty() == False
    q.pop()
    assert q.empty() == True