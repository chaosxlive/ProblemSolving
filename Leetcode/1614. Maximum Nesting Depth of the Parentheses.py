# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        maxCount = 0
        curCount = 0

        for c in s:
            if c == '(':
                curCount += 1
                if curCount > maxCount:
                    maxCount = curCount
            elif c == ')':
                curCount -= 1

        return maxCount