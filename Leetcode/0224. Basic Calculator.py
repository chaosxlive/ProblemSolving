# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current = 0
        result = 0
        op = 1
        for c in s:
            if c == '(':
                stack.append(result)
                stack.append(op)
                result = 0
                op = 1
            elif c == ')':
                result += current * op
                current = 0
                result *= stack.pop()
                result += stack.pop()
            elif c == '+':
                result += current * op
                current = 0
                op = 1
            elif c == '-':
                result += current * op
                current = 0
                op = -1
            elif c == ' ':
                pass
            else:
                current = current * 10 + int(c)
        result += current * op
        return result
