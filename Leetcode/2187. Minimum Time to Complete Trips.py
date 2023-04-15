# https://leetcode.com/problems/minimum-time-to-complete-trips/

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = min(time) * totalTrips
        result = right

        def check(total: int) -> bool:
            return sum(total // t for t in time) >= totalTrips

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
