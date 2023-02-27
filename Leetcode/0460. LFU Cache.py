# https://leetcode.com/problems/lfu-cache/

from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFrequency = None
        self.keyFrequency = {}
        self.frequencyKeys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyFrequency:
            return -1
        frequency = self.keyFrequency[key]
        val = self.frequencyKeys[frequency][key]
        del self.frequencyKeys[frequency][key]
        if not self.frequencyKeys[frequency]:
            if frequency == self.minFrequency:
                self.minFrequency += 1
            del self.frequencyKeys[frequency]
        self.keyFrequency[key] = frequency + 1
        self.frequencyKeys[frequency + 1][key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.keyFrequency:
            freq = self.keyFrequency[key]
            self.frequencyKeys[freq][key] = value
            self.get(key)
            return
        if self.capacity == len(self.keyFrequency):
            deletedKey, deletedVal = self.frequencyKeys[self.minFrequency].popitem(last=False)
            del self.keyFrequency[deletedKey]
        self.keyFrequency[key] = 1
        self.frequencyKeys[1][key] = value
        self.minFrequency = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
