# https://leetcode.com/problems/minimum-knight-moves/

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            seen = set()
            q = deque([(0, 0)])
            result = 0
            while q:
                cnt = len(q)
                for _ in range(cnt):
                    currX, currY = q.popleft()
                    if (currX, currY) == (x, y):
                        return result
                    for dx, dy in dirs:
                        nextX, nextY = currX + dx, currY + dy
                        if (nextX, nextY) not in seen:
                            seen.add((nextX, nextY))
                            q.append((nextX, nextY))
                result += 1

        return bfs(x, y)
