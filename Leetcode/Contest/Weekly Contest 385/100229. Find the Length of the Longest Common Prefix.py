from typing import List


class Node:

    def __init__(self) -> None:
        self.children = [None] * 10


class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Node()
        for num in arr1:
            ptr = root
            s = str(num)
            for c in s:
                if ptr.children[int(c)] is None:
                    ptr.children[int(c)] = Node()
                ptr = ptr.children[int(c)]
        result = 0
        for num in arr2:
            ptr = root
            s = str(num)
            l = 0
            for c in s:
                if ptr.children[int(c)] is None:
                    break
                ptr = ptr.children[int(c)]
                l += 1
            result = max(result, l)
        return result
