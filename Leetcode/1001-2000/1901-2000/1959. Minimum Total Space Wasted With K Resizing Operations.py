# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

from functools import lru_cache
from typing import List


class Solution:

    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        L = len(nums)
        if L == 1:
            return 0
        INF = 2147483647

        largers = [[-1] for _ in range(L)]
        stack = [(INF, -1), (nums[-1], L - 1)]
        for i in reversed(range(L - 1)):
            while nums[i] > stack[-1][0]:
                stack.pop()
            largers[i] = list(reversed(list(map(lambda x: x[1], stack))))
            stack.append((nums[i], i))

        @lru_cache(None)
        def solve(i: int, size: int, rest: int):
            if rest < 0:
                return INF
            if i == L - 1:
                if rest > 0:
                    return 0
                return INF if size < nums[i] else size - nums[i]
            elif size < nums[i] and rest == 0:
                return INF
            result = INF
            if size >= nums[i]:
                result = min(result, solve(i + 1, size, rest) + size - nums[i])
            for j in largers[i]:
                if j == -1:
                    j = i
                if nums[j] < nums[i]:
                    continue
                result = min(result, solve(i + 1, nums[j], rest if nums[j] == size else rest - 1) + nums[j] - nums[i])
            return result

        return min(solve(1, nums[0] if i == -1 else nums[i], k) + (nums[0] if i == -1 else nums[i]) - nums[0] for i in largers[0])
