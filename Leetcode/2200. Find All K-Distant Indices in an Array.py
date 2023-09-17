# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        return list(set(i for keyIdx, _ in filter(lambda x: x[1] == key, enumerate(nums)) for i in range(keyIdx - k, keyIdx + k + 1) if 0 <= i < len(nums)))
