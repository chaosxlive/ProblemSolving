# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        isPalindrome = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(0, len(s) - 1):
            left = right = i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                isPalindrome[left][right] = True
                left -= 1
                right += 1
            left, right = i, i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                isPalindrome[left][right] = True
                left -= 1
                right += 1
        isPalindrome[-1][-1] = True

        dp = [2147483647] * (len(s) + 1)
        dp[0] = 0
        for i in range(len(s)):
            for j in range(i + 1):
                if isPalindrome[j][i]:
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[len(s)] - 1
