import pytest

def test_push():
    stack = MinStack()
    stack.push(4)
    assert stack.stack == [4]
    assert stack.min_stack == [4]
    stack.push(2)
    assert stack.stack == [4, 2]
    assert stack.min_stack == [4, 2]
    stack.push(5)
    assert stack.stack == [4, 2, 5]
    assert stack.min_stack == [4, 2, 2]

def test_pop():
    stack = MinStack()
    stack.push(4)
    stack.push(2)
    stack.push(5)
    stack.pop()
    assert stack.stack == [4, 2]
    assert stack.min_stack == [4, 2]
    stack.pop()
    assert stack.stack == [4]
    assert stack.min_stack == [4]
    stack.pop()
    assert stack.stack == []
    assert stack.min_stack == []

def test_top():
    stack = MinStack()
    stack.push(4)
    assert stack.top() == 4
    stack.push(2)
    assert stack.top() == 2
    stack.push(5)
    assert stack.top() == 5
    stack.pop()
    assert stack.top() == 2
    stack.pop()
    assert stack.top() == 4
    stack.pop()
    assert stack.top() == None

def test_getMin():
    stack = MinStack()
    stack.push(4)
    assert stack.getMin() == 4
    stack.push(2)
    assert stack.getMin() == 2
    stack.push(5)
    assert stack.getMin() == 2
    stack.pop()
    assert stack.getMin() == 2
    stack.pop()
    assert stack.getMin() == 4
    stack.pop()
    assert stack.getMin() == None