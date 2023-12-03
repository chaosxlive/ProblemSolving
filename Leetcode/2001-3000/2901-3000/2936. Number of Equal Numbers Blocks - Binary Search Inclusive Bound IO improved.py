# https://leetcode.com/problems/number-of-equal-numbers-blocks/

from typing import Optional


# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass

class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:

        def solve(left, right, leftVal=None, rightVal=None):
            nL, nR = leftVal if leftVal else nums.at(left), rightVal if rightVal else nums.at(right)
            if nL == nR:
                return 1
            if right - left == 1:
                return 2
            mid = left + (right - left) // 2
            return solve(left, mid, leftVal=nL) + solve(mid, right, rightVal=nR) - 1

        return solve(0, nums.size() - 1)
