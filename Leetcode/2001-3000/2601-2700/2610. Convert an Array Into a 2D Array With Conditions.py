# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        result = [[] for i in range(counter.most_common(1)[0][1])]
        for v, c in counter.items():
            for i in range(c):
                result[i].append(v)
        return result
