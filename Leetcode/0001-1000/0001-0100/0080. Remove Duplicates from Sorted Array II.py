# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prevPtr = 0
        isDup = False
        curPtr = 1
        writePtr = 1
        while curPtr < len(nums):
            if nums[curPtr] == nums[prevPtr]:
                if not isDup:
                    isDup = True
                    nums[writePtr] = nums[curPtr]
                    writePtr += 1
            else:
                isDup = False
                nums[writePtr] = nums[curPtr]
                writePtr += 1
                prevPtr = curPtr
            curPtr+=1
        return writePtr