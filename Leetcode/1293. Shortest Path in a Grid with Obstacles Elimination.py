# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

import queue


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        if k > (len(grid) - 1 + len(grid[0]) - 1):
            return len(grid) - 1 + len(grid[0]) - 1
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        walked = set()
        posQueue = queue.Queue()
        posQueue.put((0, 0, k, 0))
        while not posQueue.empty():
            pos = posQueue.get()
            if tuple(pos[:3]) in walked:
                continue
            walked.add(tuple(pos[:3]))
            for d in dirs:
                nextPosRow, nextPosCol, restCnt, nextStep = pos[0] + d[0], pos[1] + d[1], pos[2], pos[3] + 1
                if (nextPosRow, nextPosCol) == (len(grid) - 1, len(grid[0]) - 1):
                    return nextStep
                if nextPosRow < 0 or nextPosRow >= len(grid) or nextPosCol < 0 or nextPosCol >= len(grid[0]):
                    continue
                if grid[nextPosRow][nextPosCol] == 1:
                    if restCnt == 0:
                        continue
                    restCnt -= 1
                posQueue.put((nextPosRow, nextPosCol, restCnt, nextStep))
        return -1
