# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def calcPenalty(maxNum):
            return sum([(num - 1) // maxNum for num in nums])

        result = 1000000001
        left, right = 1, 1000000000
        while left <= right:
            mid = left + (right - left) // 2
            operationCnt = calcPenalty(mid)
            if operationCnt <= maxOperations:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result
