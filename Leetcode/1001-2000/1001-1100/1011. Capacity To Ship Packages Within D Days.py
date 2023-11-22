# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isValid(capacity: int) -> bool:
            dayCnt = 0
            weightCnt = 0
            for w in weights:
                if weightCnt + w > capacity:
                    dayCnt += 1
                    weightCnt = 0
                weightCnt += w
            return (dayCnt if weightCnt == 0 else dayCnt + 1) <= days

        left = max(weights)
        right = sum(weights)
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            if isValid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
