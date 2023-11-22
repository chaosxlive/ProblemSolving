# https://leetcode.com/problems/evaluate-reverse-polish-notation/

import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                temp = a / b
                stack.append(math.floor(temp) if temp >= 0 else math.ceil(temp))
            else:
                stack.append(int(token))
        return stack[0]
