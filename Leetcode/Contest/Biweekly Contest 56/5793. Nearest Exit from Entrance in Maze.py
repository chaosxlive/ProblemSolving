# https://leetcode.com/contest/biweekly-contest-56/problems/nearest-exit-from-entrance-in-maze/

from queue import Queue


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        visited.add(tuple(entrance))
        next = Queue()
        for ir, ic in dirs:
            if 0 <= entrance[0] + ir < len(maze) and 0 <= entrance[1] + ic < len(maze[0]) and (entrance[0] + ir, entrance[1] + ic) not in visited and maze[entrance[0] + ir][entrance[1] + ic] == '.':
                visited.add((entrance[0] + ir, entrance[1] + ic))
                next.put((entrance[0] + ir, entrance[1] + ic, 1))

        while not next.empty():
            row, col, step = next.get()
            for ir, ic in dirs:
                if 0 <= row + ir < len(maze) and 0 <= col + ic < len(maze[0]):
                    if (row + ir, col + ic) not in visited and maze[row + ir][col + ic] == '.':
                        visited.add((row + ir, col + ic))
                        next.put((row + ir, col + ic, step + 1))
                else:
                    return step
        return -1