# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from collections import deque
from typing import List


class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        M = max(nums)
        res = 0
        for i, n in enumerate(nums):
            if n == M:
                dq.append(i)
            if len(dq) >= k:
                if len(dq) > k:
                    dq.popleft()
                res += dq[0] + 1
        return res
