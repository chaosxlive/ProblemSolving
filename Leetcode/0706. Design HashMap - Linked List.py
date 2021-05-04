# https://leetcode.com/problems/design-hashmap/

class MyHashMap:
    class ListNode:
        def __init__(self, key=None, val=None, next=None) -> None:
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = self.ListNode()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ptrPrev = None
        ptr = self.hash
        while ptr != None:
            if ptr.key == key:
                ptr.val = value
                return
            ptrPrev = ptr
            ptr = ptr.next
        newNode = self.ListNode(key, value)
        ptrPrev.next = newNode

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ptr = self.hash
        while ptr != None:
            if ptr.key == key:
                return ptr.val
            ptr = ptr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ptrPrev = None
        ptr = self.hash
        while ptr != None:
            if ptr.key == key:
                ptrPrev.next = ptr.next
                del ptr
                return
            ptrPrev = ptr
            ptr = ptr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)