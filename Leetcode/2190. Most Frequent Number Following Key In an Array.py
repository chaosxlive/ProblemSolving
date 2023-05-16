# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

from typing import List
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = defaultdict(int)
        result = (0, -1)
        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                counter[nums[i]] += 1
                if counter[nums[i]] > result[0]:
                    result = (counter[nums[i]], nums[i])
        return result[1]
