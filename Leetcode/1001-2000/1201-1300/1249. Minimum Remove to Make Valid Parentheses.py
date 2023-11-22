# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parenthese = list(filter(lambda c: c == '(' or c == ')', s))
        stack = []
        invalidParenthese = set()
        for i, p in enumerate(parenthese):
            if p == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    invalidParenthese.add(i)
                else:
                    stack.pop()
        invalidParenthese.update(stack)
        validParenthese = []
        for i, p in enumerate(parenthese):
            if i not in invalidParenthese:
                validParenthese.append(p)
        result = []
        idx = 0
        for c in s:
            if c == '(' or c == ')':
                if idx < len(validParenthese) and validParenthese[idx] == c:
                    result.append(c)
                    idx += 1
            else:
                result.append(c)
        return ''.join(result)
