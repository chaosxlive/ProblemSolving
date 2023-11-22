# https://leetcode.com/problems/magnetic-force-between-two-balls/

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(gap, m):
            cnt = 1
            prevPlaced = position[0]
            idx = 1
            while cnt < m:
                if idx >= len(position):
                    return False
                if position[idx] - prevPlaced >= gap:
                    prevPlaced = position[idx]
                    cnt += 1
                idx += 1
            return True

        result = 0
        left, right = 1, (position[-1] - position[0]) // (m - 1)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid, m):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
