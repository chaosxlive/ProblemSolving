# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(result, current, countL, countR, target):
            if countR == target:
                result.append("".join(current))
                return

            if countL < target:
                current.append("(")
                backtrack(result, current, countL + 1, countR, target)
                current.pop()
            if countR < countL:
                current.append(")")
                backtrack(result, current, countL, countR + 1, target)
                current.pop()

        result = []
        backtrack(result, [], 0, 0, n)
        return result
