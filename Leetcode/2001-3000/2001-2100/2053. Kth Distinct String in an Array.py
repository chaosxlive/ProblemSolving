# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        count = 0
        for key, val in counter.items():
            if val == 1:
                count += 1
                if count == k:
                    return key
        return ""
