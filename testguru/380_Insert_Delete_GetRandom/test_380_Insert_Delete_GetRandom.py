#test_insert tests the insert method of the RandomizedSet class
def test_insert():
  rs = RandomizedSet()
  assert rs.insert(1) == True
  assert rs.insert(2) == True
  assert rs.insert(1) == False

#test_remove tests the remove method of the RandomizedSet class
def test_remove():
  rs = RandomizedSet()
  rs.insert(1)
  rs.insert(2)
  assert rs.remove(3) == False
  assert rs.remove(1) == True
  assert rs.remove(1) == False

#test_getRandom tests the getRandom method of the RandomizedSet class
def test_getRandom():
  rs = RandomizedSet()
  rs.insert(1)
  rs.insert(2)
  rs.insert(3)
  assert rs.getRandom() in [1,2,3]

#test_combined tests the insert, remove and getRandom method of the RandomizedSet class
def test_combined():
  rs = RandomizedSet()
  assert rs.insert(1) == True
  assert rs.insert(2) == True
  assert rs.insert(3) == True
  assert rs.remove(4) == False
  assert rs.remove(1) == True
  assert rs.getRandom() in [2,3]