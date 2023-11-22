# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = set()
        visited.add((0, 0))
        commands = {'N': [0, 1], 'E': [1, 0], 'W': [-1, 0], 'S': [0, -1]}
        for c in path:
            x += commands[c][0]
            y += commands[c][1]
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
