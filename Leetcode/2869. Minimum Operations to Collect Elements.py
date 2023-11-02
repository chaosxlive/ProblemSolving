# https://leetcode.com/problems/minimum-operations-to-collect-elements/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        valids = [False] * (k + 1)
        cnt = 0
        for i, num in enumerate(reversed(nums)):
            if num >= 1 and num <= k and not valids[num]:
                valids[num] = True
                cnt += 1
                if cnt == k:
                    return i + 1
        return len(nums)
