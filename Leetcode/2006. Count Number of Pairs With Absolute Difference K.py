# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        result = 0
        for num in nums:
            result += count[num + k] + count[num - k]
            count[num] += 1
        return result
