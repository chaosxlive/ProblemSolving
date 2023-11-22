# https://leetcode.com/problems/constrained-subsequence-sum/

from typing import List
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        d = deque()
        result = -2147483648
        for i, num in enumerate(nums):
            while len(d) > 0 and d[0][1] + k < i:
                d.popleft()
            if len(d) > 0:
                tmp = max(d[0][0] + num, num)
                result = max(result, tmp)
                while len(d) > 0 and tmp >= d[-1][0]:
                    d.pop()
                d.append((tmp, i))
            else:
                result = max(result, num)
                d.append((num, i))
        return result
