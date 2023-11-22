# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""

        layer = 0
        for c in S:
            if c == "(":
                if layer != 0:
                    result += "("
                layer += 1
            elif c == ")":
                layer -= 1
                if layer != 0:
                    result += ")"
        return result
