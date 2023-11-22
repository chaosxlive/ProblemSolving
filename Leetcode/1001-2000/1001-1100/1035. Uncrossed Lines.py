# https://leetcode.com/problems/uncrossed-lines/

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0 for i in range(len(nums1) + 1)]
        for n2 in nums2:
            prev = 0
            for i, n1 in enumerate(nums1):
                temp = dp[i + 1]
                if n1 == n2:
                    dp[i + 1] = prev + 1
                else:
                    dp[i + 1] = max(dp[i], dp[i + 1])
                prev = temp
        return dp[-1]
