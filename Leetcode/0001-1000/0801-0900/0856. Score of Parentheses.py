# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        def getScore(s, start):
            if s[start] == ')':
                return 1, start + 1
            result = 0
            index = start
            while index < len(s):
                if s[index] == '(':
                    score, index = getScore(s, index + 1)
                    result += score * 2
                else:
                    break
                
            return result, index + 1

        result, index = getScore(s, 0)
        return result // 2
