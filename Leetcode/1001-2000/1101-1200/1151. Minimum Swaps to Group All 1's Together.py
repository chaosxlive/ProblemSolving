# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        result = len(data)
        oneCount = data.count(1)
        if oneCount == 0:
            return 0
        windowCnt = sum(data[:oneCount - 1])
        for i in range(len(data) - oneCount + 1):
            windowCnt += data[i + oneCount - 1]
            result = min(result, oneCount - windowCnt)
            windowCnt -= data[i]
        return result
