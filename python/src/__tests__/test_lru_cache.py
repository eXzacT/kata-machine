from src.lru_cache import LRUCache, LRUCacheOrderedDict


def test_lru_cache():
    lru = LRUCache(2)
    lru.put(1, 1)  # cache is {1=1}
    lru.put(2, 2)  # cache is {1=1, 2=2}
    assert lru.get(1) == 1
    lru.put(3, 3)  # Used 1 by getting it, so 2 will be LRU and kicked
    assert lru.get(2) == -1  # Not found
    lru.put(4, 4)  # Since we added 3 last time, LRU is 1 and we kick it
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    lru = LRUCache(1)
    lru.put(2, 1)
    assert lru.get(2) == 1
    lru.put(3, 2)
    assert lru.get(2) == -1
    assert lru.get(3) == 2


def test_lru_cache_ordered_dict():
    lru = LRUCacheOrderedDict(2)
    lru.put(1, 1)  # cache is {1=1}
    lru.put(2, 2)  # cache is {1=1, 2=2}
    assert lru.get(1) == 1
    lru.put(3, 3)  # Used 1 by getting it, so 2 will be LRU and kicked
    assert lru.get(2) == -1  # Not found
    lru.put(4, 4)  # Since we added 3 last time, LRU is 1 and we kick it
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    lru = LRUCacheOrderedDict(1)
    lru.put(2, 1)
    assert lru.get(2) == 1
    lru.put(3, 2)
    assert lru.get(2) == -1
    assert lru.get(3) == 2
