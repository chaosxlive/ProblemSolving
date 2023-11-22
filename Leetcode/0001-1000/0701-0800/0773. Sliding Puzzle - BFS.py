# https://leetcode.com/problems/

from queue import SimpleQueue


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def copyBoard(board):
            result = []
            for row in board:
                result.append(row[:])
            return result

        def getBoardHashable(board):
            result = []
            for row in board:
                result.append(tuple(row))
            return tuple(result)

        def checkBoard(board):
            for row in range(2):
                for col in range(3):
                    if board[row][col] != row * 3 + col + 1 and (row != 1 or col != 2):
                        return False
            return True

        def findZero(board):
            for row in range(2):
                for col in range(3):
                    if board[row][col] == 0:
                        return [row, col]

        def addPossible(queue, seen, board, count):
            zeroRow, zeroCol = findZero(board)
            if zeroRow > 0:  # Up
                tempBoard = copyBoard(board)
                tempBoard[zeroRow][zeroCol], tempBoard[zeroRow - 1][zeroCol] = tempBoard[zeroRow - 1][zeroCol], tempBoard[zeroRow][zeroCol]
                tempBoardHashable = getBoardHashable(tempBoard)
                if tempBoardHashable not in seen:
                    queue.put((tempBoard, count))
                    seen.add(tempBoardHashable)
            if zeroCol > 0:  # Left
                tempBoard = copyBoard(board)
                tempBoard[zeroRow][zeroCol], tempBoard[zeroRow][zeroCol - 1] = tempBoard[zeroRow][zeroCol - 1], tempBoard[zeroRow][zeroCol]
                tempBoardHashable = getBoardHashable(tempBoard)
                if tempBoardHashable not in seen:
                    queue.put((tempBoard, count))
                    seen.add(tempBoardHashable)
            if zeroRow < 1:  # Down
                tempBoard = copyBoard(board)
                tempBoard[zeroRow][zeroCol], tempBoard[zeroRow + 1][zeroCol] = tempBoard[zeroRow + 1][zeroCol], tempBoard[zeroRow][zeroCol]
                tempBoardHashable = getBoardHashable(tempBoard)
                if tempBoardHashable not in seen:
                    queue.put((tempBoard, count))
                    seen.add(tempBoardHashable)
            if zeroCol < 2:  # Right
                tempBoard = copyBoard(board)
                tempBoard[zeroRow][zeroCol], tempBoard[zeroRow][zeroCol + 1] = tempBoard[zeroRow][zeroCol + 1], tempBoard[zeroRow][zeroCol]
                tempBoardHashable = getBoardHashable(tempBoard)
                if tempBoardHashable not in seen:
                    queue.put((tempBoard, count))
                    seen.add(tempBoardHashable)

        queue = SimpleQueue()
        queue.put((board, 0))
        seen = set()

        while not queue.empty():
            currentBoard, count = queue.get()
            if checkBoard(currentBoard):
                return count
            addPossible(queue, seen, currentBoard, count + 1)
        return -1
