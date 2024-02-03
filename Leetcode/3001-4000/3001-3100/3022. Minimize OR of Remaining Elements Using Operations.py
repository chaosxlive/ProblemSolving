# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

from typing import List


class Solution:

    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        bit = 1 << 31
        mask = 0
        result = 0
        while bit > 0:
            currMask = mask | bit
            cnt = 0
            rest = nums[0] & currMask
            isPrevZero = rest == 0
            for i in range(1, len(nums)):
                num = nums[i] & currMask
                if num > 0:
                    if rest == 0:
                        rest = num
                    else:
                        cnt += 1
                        rest &= num
                        if rest == 0:
                            isPrevZero = True
                else:
                    isPrevZero = True
                    if rest > 0:
                        cnt += 1
                        rest = 0
            isEliminable = True
            if rest > 0:
                if isPrevZero:
                    cnt += 1
                else:
                    isEliminable = False

            if isEliminable and cnt <= k:
                mask |= bit
            else:
                result |= bit
            bit >>= 1
        return result
