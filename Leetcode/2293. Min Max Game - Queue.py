# https://leetcode.com/problems/min-max-game/

from collections import deque


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        q = deque(nums)
        isEven = True
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            if isEven:
                q.append(min(a, b))
            else:
                q.append(max(a, b))
            isEven = not isEven
        return q.popleft()
