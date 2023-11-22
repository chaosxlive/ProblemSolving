# https://leetcode.com/problems/split-array-with-equal-sum/

from itertools import accumulate


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        if len(nums) < 7:
            return False
        prefixSum = [0] + list(accumulate(nums))

        for i in range(3, len(nums) - 3):
            possible = set()
            for j in range(1, i - 1):
                left = prefixSum[j]
                right = prefixSum[i] - prefixSum[j + 1]
                if left == right:
                    possible.add(left)
            for j in range(i + 2, len(nums) - 1):
                left = prefixSum[j] - prefixSum[i + 1]
                right = prefixSum[len(nums)] - prefixSum[j + 1]
                if left == right and left in possible:
                    return True
        return False
