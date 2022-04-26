# https://leetcode.com/problems/array-of-doubled-pairs/

from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for key in sorted(arr, key=abs):
            if count[key] == 0:
                continue
            if count[2 * key] == 0:
                return False
            count[key] -= 1
            count[2 * key] -= 1
        return True
