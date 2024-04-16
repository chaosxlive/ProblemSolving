# https://leetcode.com/problems/robot-bounded-in-circle/


class Solution:

    def isRobotBounded(self, instructions: str) -> bool:
        currX = currY = currD = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for _ in range(4):
            for ins in instructions:
                if ins == 'L':
                    currD -= 1
                    currD %= 4
                elif ins == 'R':
                    currD += 1
                    currD %= 4
                else:
                    dx, dy = dirs[currD]
                    currX += dx
                    currY += dy
            if (currX, currY, currD) == (0, 0, 0):
                return True
        return False
