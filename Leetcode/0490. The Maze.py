# https://leetcode.com/problems/the-maze/

import queue


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        walked = set()
        nextPath = queue.Queue()
        walked.add((start[0], start[1]))
        for d in range(4):
            nextPath.put((d, start[0], start[1]))

        def move(d, x, y):
            if isNextWall(d, x, y):
                return False
            while True:
                x += dirs[d][0]
                y += dirs[d][1]
                if isNextWall(d, x, y):
                    if (x, y) in walked:
                        return False
                    if destination[0] == x and destination[1] == y:
                        return True
                    walked.add((x, y))
                    for d in range(4):
                        nextPath.put((d, x, y))
                    break
            return False

        def isNextWall(d, x, y):
            if (x + dirs[d][0] < 0 or x + dirs[d][0] >= len(maze) or y + dirs[d][1] < 0 or y + dirs[d][1] >= len(maze[0])):
                return True
            return maze[x + dirs[d][0]][y + dirs[d][1]] == 1

        while not nextPath.empty():
            [d, x, y] = nextPath.get()
            if move(d, x, y):
                return True
        return False
