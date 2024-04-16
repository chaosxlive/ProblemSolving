# https://leetcode.com/problems/ant-on-the-boundary/

from typing import List


class Solution:

    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        result = 0
        for num in nums:
            pos += num
            if pos == 0:
                result += 1

        return result
