import pytest 

@pytest.fixture
def cache():
    return LRUCache(2)

def test_cache_insertion(cache):
    cache.put(1, 1)
    assert cache.cache == {1:1}
    assert cache.queue == [1]

def test_cache_insert_max_size(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.cache == {2:2, 3:3}
    assert cache.queue == [3, 2]

def test_cache_insert_reorder(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    assert cache.cache == {1:1, 3:3}
    assert cache.queue == [3, 1]
    
def test_cache_get(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

def test_cache_get_not_exists(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(3) == -1

def test_cache_put_overwrite(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    assert cache.cache == {1:10, 2:2}
    assert cache.queue == [1, 2]