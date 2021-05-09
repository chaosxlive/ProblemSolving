# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'D':
                y += 1
            elif move == 'U':
                y -= 1
            elif move == 'R':
                x += 1
            else:
                x -= 1
        return x == y == 0
