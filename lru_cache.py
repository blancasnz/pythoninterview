from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        self.store = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.store:
            return -1

        val = self.store.pop(key)
        self.store[key] = val
        return val

    def put(self, key, val):
        if key in self.store:
            self.store.pop(key)
        elif len(self.store) == self.capacity:
            self.store.popitem(last=False)
        self.store[key] = val
