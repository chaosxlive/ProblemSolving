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
            nL, nR = leftVal if leftVal else nums.at(left), rightVal if rightVal else nums.at(right - 1)
            if nL == nR:
                return (nL, 1, nR)
            if right - left == 2:
                return (nL, 2, nR)
            mid = left + (right - left) // 2
            _, resL, rightL = solve(left, mid, leftVal=nL)
            leftR, resR, _ = solve(mid, right, rightVal=nR)
            return (nL, resL + resR - 1 if rightL == leftR else resL + resR, nR)

        return solve(0, nums.size())[1]
