# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        result = 0
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    result = max(result, dp[i][j])
        return result
