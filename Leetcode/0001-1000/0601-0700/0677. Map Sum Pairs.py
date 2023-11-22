# https://leetcode.com/problems/map-sum-pairs/

class TreeNode:
    def __init__(self, sum=0, next=None, isEnd=0):
        self.sum = sum
        self.next = [None] * 26
        self.isEnd = isEnd


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = TreeNode()

    def insert(self, key: str, val: int) -> None:
        origin_val = 0
        iter_check = self.start
        isMatch = True
        for c in key:
            if iter_check.next[ord(c) - 97] == None:
                isMatch = False
                break
            iter_check = iter_check.next[ord(c) - 97]
        if isMatch:
            origin_val = iter_check.isEnd

        iter_node = self.start
        for c in key:
            if iter_node.next[ord(c) - 97] == None:
                iter_node.next[ord(c) - 97] = TreeNode()
            iter_node = iter_node.next[ord(c) - 97]
            iter_node.sum += val - origin_val
        iter_node.isEnd = val

    def sum(self, prefix: str) -> int:
        iter_node = self.start
        for c in prefix:
            if iter_node.next[ord(c) - 97] == None:
                return 0
            iter_node = iter_node.next[ord(c) - 97]
        return iter_node.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
