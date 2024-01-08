# https://leetcode.com/problems/candy-crush/

from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        H, W = len(board), len(board[0])
        marks = [[False] * W for _ in range(H)]
        isChanged = True

        def markTrueX(y: int, start: int, end: int):
            nonlocal isChanged
            isChanged = True
            for i in range(start, end):
                marks[y][i] = True

        def markTrueY(x: int, start: int, end: int):
            nonlocal isChanged
            isChanged = True
            for i in range(start, end):
                marks[i][x] = True

        def markClear():
            nonlocal isChanged
            isChanged = False
            for x in range(W):
                low = high = H - 1
                while high >= 0:
                    while high >= 0 and marks[high][x]:
                        marks[high][x] = False
                        high -= 1
                    if high < 0:
                        break
                    board[low][x] = board[high][x]
                    low -= 1
                    high -= 1
                while low >= 0:
                    board[low][x] = 0
                    low -= 1

        while isChanged:
            markClear()
            for y in range(H):
                prev = 0
                x = 1
                while x < W:
                    if board[y][x] == 0:
                        if x - prev >= 3:
                            markTrueX(y, prev, x)
                        prev = x
                    elif board[y][x] != board[y][prev]:
                        if x - prev >= 3:
                            markTrueX(y, prev, x)
                        prev = x
                    x += 1
                if x - prev >= 3:
                    markTrueX(y, prev, x)
            for x in range(W):
                prev = 0
                y = 1
                while y < H:
                    if board[y][x] == 0:
                        if y - prev >= 3:
                            markTrueY(x, prev, y)
                        prev = y
                    elif board[y][x] != board[prev][x]:
                        if y - prev >= 3:
                            markTrueY(x, prev, y)
                        prev = y
                    y += 1
                if y - prev >= 3:
                    markTrueY(x, prev, y)

        return board
