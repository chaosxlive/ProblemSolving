# https://leetcode.com/problems/lru-cache/

class LinkedList:

    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = [None] * 100001
        self.capacity = capacity
        self.size = 0
        self.valuesHead = LinkedList(0)
        self.valuesTail = self.valuesHead

    def get(self, key: int) -> int:
        if self.cache[key] == None:
            return -1

        node = self.cache[key]
        
        if node == self.valuesTail:
            return node.val

        node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        node.prev = self.valuesTail
        node.next = None
        self.valuesTail.next = node
        self.valuesTail = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cache[key] != None:
            node = self.cache[key]
            node.val = value
        
            if node == self.valuesTail:
                return

            node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            node.prev = self.valuesTail
            node.next = None
            self.valuesTail.next = node
            self.valuesTail = node
        else:
            node = LinkedList(key, value, self.valuesTail)
            self.cache[key] = node
            self.size += 1
            self.valuesTail.next = node
            self.valuesTail = node

            if self.size > self.capacity:
                node = self.valuesHead.next
                self.valuesHead.next = node.next
                node.next.prev = self.valuesHead
                self.cache[node.key] = None
                del node
