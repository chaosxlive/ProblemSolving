# https://leetcode.com/problems/minimize-maximum-of-array/

from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left, right = 0, max(nums)

        def check(threshold):
            rest = 0
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] + rest > threshold:
                    rest = nums[i] + rest - threshold
                else:
                    rest = 0
            return nums[0] + rest <= threshold

        result = right
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result
