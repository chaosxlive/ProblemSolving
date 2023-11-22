# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '(':
                    return False
            elif c == '[':
                stack.append('[')
            elif c == ']':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '[':
                    return False
            elif c == '{':
                stack.append('{')
            elif c == '}':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '{':
                    return False
        
        return len(stack) == 0
