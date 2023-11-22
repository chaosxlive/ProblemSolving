# https://leetcode.com/problems/snakes-and-ladders/

from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def getIdx(pos):
            r, c = divmod(pos - 1, n)
            if r % 2 == 0:
                return (n - 1 - r, c)
            else:
                return (n - 1 - r, n - 1 - c)

        visited = set()
        q = deque([])
        q.append((1, 0))
        while q:
            currentPos, stepNum = q.popleft()
            r, c = getIdx(currentPos)
            if board[r][c] != -1:
                currentPos = board[r][c]
            if currentPos == n * n:
                return stepNum
            for nextPos in range(currentPos + 1, min(currentPos + 6, n * n) + 1):
                if nextPos not in visited:
                    visited.add(nextPos)
                    q.append((nextPos, stepNum + 1))
        return -1
