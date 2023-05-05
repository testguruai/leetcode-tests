import pytest

def test_push():
    s = Stack()
    s.push(1)
    assert s.queue1 == [1]
    assert s.queue2 == []
    assert s.curr_top == 1
    
    s.push(2)
    assert s.queue1 == [2,1]
    assert s.queue2 == []
    assert s.curr_top == 2
    
    s.push(3)
    assert s.queue1 == [3,2,1]
    assert s.queue2 == []
    assert s.curr_top == 3
    
def test_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    s.pop()
    assert s.queue1 == [2,1]
    assert s.queue2 == []
    assert s.curr_top == 2
    
    s.pop()
    assert s.queue1 == [1]
    assert s.queue2 == []
    assert s.curr_top == 1
    
    s.pop()
    assert s.queue1 == []
    assert s.queue2 == []
    assert s.curr_top == 0
    
def test_top():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    assert s.top() == 3
    
    s.pop()
    assert s.top() == 2
    
    s.pop()
    assert s.top() == 1
    
    s.pop()
    assert s.top() == None
    
def test_empty():
    s = Stack()
    assert s.empty() == True
    
    s.push(1)
    assert s.empty() == False
    
    s.pop()
    assert s.empty() == True