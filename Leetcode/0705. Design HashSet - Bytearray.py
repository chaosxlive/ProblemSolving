# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = bytearray(1000001) 

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key: int) -> None:
        self.hash[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hash[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
