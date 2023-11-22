# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        result = 0
        for op in ops:
            if op == '+':
                result += scores[-1] + scores[-2]
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                result += scores[-1] * 2
                scores.append(scores[-1] * 2)
            elif op == 'C':
                result -= scores[-1]
                scores.pop()
            else:
                result += int(op)
                scores.append(int(op))
        return result