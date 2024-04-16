# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

from collections import Counter
from typing import List


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = sorted(Counter(arr).values(), reverse=True)
        result = len(counter)
        i = 0
        while k > 0:
            if k < counter[i]:
                break
            k -= counter[i]
            i += 1
        return result
