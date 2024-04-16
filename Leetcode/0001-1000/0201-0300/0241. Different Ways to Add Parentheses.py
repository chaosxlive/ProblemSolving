# https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List


class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        parts = []
        prev = curr = 0
        while curr < len(expression):
            if expression[curr] in '+-*':
                parts.append(int(expression[prev:curr]))
                parts.append(expression[curr])
                prev = curr + 1
                curr += 2
            else:
                curr += 1
        parts.append(int(expression[prev:]))

        result = []

        def solve(prevs, i):
            curr = parts[i]
            if i + 1 < len(parts):
                solve(prevs[:] + [parts[i], parts[i + 1]], i + 2)
            while len(prevs) > 0:
                op = prevs.pop()
                prev = prevs.pop()
                if op == '+':
                    curr = prev + curr
                elif op == '-':
                    curr = prev - curr
                else:
                    curr = prev * curr
                if i + 1 < len(parts):
                    solve(prevs[:] + [curr, parts[i + 1]], i + 2)
            if i + 1 >= len(parts):
                result.append(curr)

        solve([], 0)
        return result
