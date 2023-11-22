# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

from typing import List
import math


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        def getLevel(n):
            return math.floor(math.log2(n)) + 1

        result = [label]
        while True:
            label //= 2
            if label < 1:
                break
            level = getLevel(label)
            end = int(math.pow(2, level))
            start = end // 2
            label = end - 1 - label + start
            result.append(label)
        return list(reversed(result))
