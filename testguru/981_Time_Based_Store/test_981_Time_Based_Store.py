
import pytest
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        values = self.store.get(key, [])
        res = ""

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        
        return res

def test_set():
    time_map = TimeMap()
    time_map.set("a", "apple", 1)
    values = time_map.store["a"]
    assert values == [("apple", 1)]

def test_get():
    time_map = TimeMap()
    time_map.set("a", "apple", 1)
    assert time_map.get("a", 0) == ""
    assert time_map.get("a", 1) == "apple"

def test_multiple_set():
    time_map = TimeMap()
    time_map.set("a", "apple", 1)
    time_map.set("a", "apricot", 2)
    time_map.set("b", "banana", 1)
    assert time_map.store == {"a": [("apple", 1), ("apricot", 2)], "b": [("banana", 1)]}

def test_empty_key():
    time_map = TimeMap()
    assert time_map.get("", 0) == ""
    time_map.set("", "empty", 1)
    assert time_map.get("", 1) == "empty"
