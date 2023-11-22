# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        marks = [False] * len(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif len(stack) > 0:
                marks[stack.pop()] = True
                marks[i] = True
        result = 0
        cnt = 0
        for v in marks:
            if v:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 0
        return max(result, cnt)
