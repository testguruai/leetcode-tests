import pytest
from solution import MyHashMap

def test_put_get_remove():
    #Testcase to check basic fuctionality
    hashMap = MyHashMap()
    hashMap.put(1,1)
    hashMap.put(2,2)
    assert hashMap.get(1) == 1
    assert hashMap.get(3) == -1
    hashMap.put(2, 1)
    assert hashMap.get(2) == 1
    hashMap.remove(2)
    assert hashMap.get(2) == -1

def test_empty():
    #Testcase when hashmap is empty
    hashMap = MyHashMap()
    assert hashMap.get(2) == -1

def test_duplicate():
    #Testcase to test duplicates
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(1, 2)
    assert hashMap.get(1) == 2

def test_remove_nonexistant():
    #Testcase to test removing a non-existent element
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.remove(2)
    assert hashMap.get(1) == 1

if __name__ == '__main__':
    pytest.main()
