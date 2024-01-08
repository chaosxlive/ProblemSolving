# https://leetcode.com/problems/queries-on-a-permutation-with-key/

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nums = [i for i in range(1, m+1)]
        result = []
        for q in queries:
            i = nums.index(q)
            nums.pop(i)
            nums.insert(0, q)
            result.append(i)
        return result
