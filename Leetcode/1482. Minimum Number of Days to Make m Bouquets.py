# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        if m * k == len(bloomDay):
            return max(bloomDay)

        def check(day, m, k):
            prev = -1
            cnt = 0
            for i, d in enumerate(bloomDay):
                if d > day:
                    cnt += (i - prev - 1) // k
                    prev = i
            cnt += (len(bloomDay) - prev - 1) // k
            return cnt >= m

        candidates = sorted(set(bloomDay))
        result = 2147483647
        left, right = 0, len(candidates) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if check(candidates[mid], m, k):
                result = candidates[mid]
                right = mid - 1
            else:
                left = mid + 1
        return result
