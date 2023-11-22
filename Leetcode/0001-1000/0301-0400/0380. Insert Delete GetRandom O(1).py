# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:

    def __init__(self):
        self.container = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:
        if val in self.indexMap:
            return False
        self.indexMap[val] = len(self.container)
        self.container.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        self.indexMap[self.container[-1]] = self.indexMap[val]
        self.container[self.indexMap[val]] = self.container[-1]
        self.indexMap.pop(val)
        self.container.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.container)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
