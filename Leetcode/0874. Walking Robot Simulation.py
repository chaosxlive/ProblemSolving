# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(lambda x: (x[0], x[1]), obstacles))
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        currentDir = 0
        currentX = currentY = 0
        result = 0
        for command in commands:
            if command == -2:
                currentDir -= 1
                if currentDir == -1:
                    currentDir = 3
            elif command == -1:
                currentDir += 1
                if currentDir == 4:
                    currentDir = 0
            else:
                step = command
                while step > 0:
                    if (currentX + directions[currentDir][0], currentY + directions[currentDir][1]) in obstacles:
                        break
                    currentX += directions[currentDir][0]
                    currentY += directions[currentDir][1]
                    step -= 1
                result = max(result, currentX * currentX + currentY * currentY)
        return result
