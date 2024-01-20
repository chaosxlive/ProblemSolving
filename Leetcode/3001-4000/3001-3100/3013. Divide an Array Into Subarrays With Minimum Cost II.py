# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

from typing import List
from sortedcontainers import SortedList


class Solution:

    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        L = len(nums)
        k -= 1
        candidates = sorted(nums[1:dist + 2])
        currMins = SortedList(candidates[:k])
        candidateMins = SortedList(candidates[k:])
        result = sum(currMins)
        curr = result
        for i in range(1, L - dist - 1):
            if nums[i] in currMins:
                curr -= nums[i]
                currMins.remove(nums[i])
            else:
                candidateMins.remove(nums[i])
            if len(currMins) == 0 or nums[i + dist + 1] <= currMins[-1]:
                currMins.add(nums[i + dist + 1])
                curr += nums[i + dist + 1]
            else:
                candidateMins.add(nums[i + dist + 1])
            if len(currMins) > k:
                curr -= currMins[-1]
                candidateMins.add(currMins.pop())
            elif len(currMins) < k:
                curr += candidateMins[0]
                currMins.add(candidateMins.pop(0))
            result = min(result, curr)
        return nums[0] + result
