# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        left = right = 0
        stack = []
        while True:
            if right == len(s):
                stack.append(int(s[left:right]))
                break
            elif s[right] in '+-*/':
                stack.append(int(s[left:right]))
                stack.append(s[right])
                left = right + 1
            right += 1
        for i in range(1, len(stack) - 1, 2):
            if stack[i] == '*':
                stack[i + 1] = stack[i - 1] * stack[i + 1]
                stack[i] = '-' if i >= 2 and stack[i - 2] == '-' else '+'
                stack[i - 1] = 0
            elif stack[i] == '/':
                stack[i + 1] = stack[i - 1] // stack[i + 1]
                stack[i] = '-' if i >= 2 and stack[i - 2] == '-' else '+'
                stack[i - 1] = 0
        for i in range(1, len(stack) - 1, 2):
            if stack[i] == '+':
                stack[0] += stack[i + 1]
            elif stack[i] == '-':
                stack[0] -= stack[i + 1]
        return stack[0]
