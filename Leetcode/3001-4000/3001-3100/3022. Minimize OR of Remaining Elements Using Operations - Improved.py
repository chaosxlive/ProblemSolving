# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

from typing import List


class Solution:

    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        mask = result = 0
        for i in reversed(range(31)):
            bit = 1 << i
            currMask = mask | bit
            cnt = 0
            rest = 0
            for num in nums:
                if rest == 0:
                    rest = num & currMask
                else:
                    rest &= num
                if rest:
                    cnt += 1
            if cnt > k:
                result |= bit
            else:
                mask |= bit
        return result
