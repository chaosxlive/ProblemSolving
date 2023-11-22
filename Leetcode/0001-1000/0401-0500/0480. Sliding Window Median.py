# https://leetcode.com/problems/sliding-window-median/

from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        subArray = SortedList()
        for i in range(k - 1):
            subArray.add(nums[i])
        result = []
        for i in range(k - 1, len(nums)):
            subArray.add(nums[i])
            if k % 2 == 0:
                result.append((subArray[k // 2] + subArray[k // 2 - 1]) / 2)
            else:
                result.append(subArray[k // 2])
            subArray.remove(nums[i - k + 1])
        return result
