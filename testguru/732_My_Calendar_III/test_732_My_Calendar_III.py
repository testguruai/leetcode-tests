
import pytest
from solution import MyCalendarThree

def test_book():
  c = MyCalendarThree()
  assert c.book(10, 20) == 1
  assert c.book(50, 60) == 1
  assert c.book(10, 40) == 2
  assert c.book(5, 15) == 3
  assert c.book(25, 55) == 3
  assert c.book(70, 80) == 1

def test_book_invalid():
  c = MyCalendarThree()
  with pytest.raises(TypeError):
    c.book('a', 'b')
  with pytest.raises(ValueError):
    c.book(20, 10)
    c.book(30, 30)
    
def test_duplicate_events():
  c = MyCalendarThree()
  assert c.book(10, 20) == 1
  assert c.book(10, 20) == 2
  assert c.book(30, 40) == 2
  assert c.book(30, 40) == 3
