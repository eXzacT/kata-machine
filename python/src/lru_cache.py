from collections import OrderedDict

''' Implement the LRUCache class:

    LRUCache(int capacity): 
        Initialize the LRU cache with positive size capacity.
    int get(int key):
        Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value):
        Update the value of the key if the key exists. 
        Otherwise, add the key-value pair to the cache. 
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.'''


class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.nxt = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def __remove(self, node: ListNode) -> None:
        if node.nxt:
            node.nxt.prev = node.prev
        if node.prev:
            node.prev.nxt = node.nxt

    def __insert(self, node: ListNode) -> None:
        node.nxt = self.right
        node.prev = self.right.prev
        node.prev.nxt = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.__remove(node)  # Remove wherever it is
            self.__insert(node)  # Move to the front
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.__remove(self.cache[key])

        self.cache[key] = ListNode(key, val)
        self.__insert(self.cache[key])

        # Have to kick LRU out
        if len(self.cache) > self.capacity:
            lru = self.left.nxt  # Dummy node always points to it
            self.__remove(lru)
            del self.cache[lru.key]


class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = val
        if len(self.cache.keys()) > self.capacity:
            self.cache.popitem(0)
