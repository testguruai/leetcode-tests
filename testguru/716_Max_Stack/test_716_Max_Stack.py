import pytest

def test_push():
    stack = MaxStack()
    stack.push(1)
    stack.push(2)
    assert stack.stack == [1, 2]
    assert stack.max_stack == [1, 2]

def test_pop():
    stack = MaxStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.stack == [1]
    assert stack.max_stack == [1]

def test_top():
    stack = MaxStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.stack == [1, 2]
    assert stack.max_stack == [1, 2]

def test_peekMax():
    stack = MaxStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peekMax() == 3
    assert stack.stack == [1, 2, 3]
    assert stack.max_stack == [1, 2, 3]

def test_popMax():
    stack = MaxStack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    assert stack.popMax() == 3
    assert stack.stack == [1, 2]
    assert stack.max_stack == [1, 2]