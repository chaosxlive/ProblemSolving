# https://leetcode.com/problems/minesweeper/

from queue import Queue


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        directions = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
        next = Queue()
        next.put(tuple(click))
        visited = set()
        visited.add(tuple(click))
        while not next.empty():
            row, col = next.get()
            count = 0
            for direction in directions:
                if 0 <= row + direction[0] < len(board) and 0 <= col + direction[1] < len(board[0]):
                    if board[row + direction[0]][col + direction[1]] == 'M':
                        count += 1
            if count == 0:
                board[row][col] = 'B'
                for direction in directions:
                    if 0 <= row + direction[0] < len(board) and 0 <= col + direction[1] < len(board[0]):
                        if (row + direction[0], col + direction[1]) not in visited:
                            next.put((row + direction[0], col + direction[1]))
                            visited.add((row + direction[0], col + direction[1]))
            else:
                board[row][col] = str(count)

        return board
