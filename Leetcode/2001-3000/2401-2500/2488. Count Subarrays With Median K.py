# https://leetcode.com/problems/count-subarrays-with-median-k/

from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        idxK = -1
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i] = -1
            elif nums[i] > k:
                nums[i] = 1
            else:
                nums[i] = 0
                idxK = i
        sums = [0] * len(nums)
        right = defaultdict(lambda: 0)
        s = 0
        for i in range(idxK, len(nums)):
            s += nums[i]
            right[s] += 1
        result = 0
        s = 0
        for i in range(idxK, -1, -1):
            s += nums[i]
            result += right[-s]
            result += right[-s + 1]
        return result
