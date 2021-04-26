# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        board = [[0 for col in range(len(M[0]) + 2)]]
        for row in M:
            board.append([0] + row[:] + [0])
        board.append([0 for col in range(len(M[0]) + 2)])

        result = [[0 for col in range(len(M[0]))] for row in range(len(M))]

        for row in range(1, len(M) + 1):
            for col in range(1, len(M[0]) + 1):
                summary = board[row - 1][col - 1] + board[row - 1][col] + board[row - 1][col + 1] +\
                    board[row][col - 1] + board[row][col] + board[row][col + 1] +\
                    board[row + 1][col - 1] + board[row + 1][col] + board[row + 1][col + 1]
                if row == 1 and row == len(M):
                    if col == 1 and col == len(M[0]):
                        result[row - 1][col - 1] = summary
                    elif col == 1 or col == len(M[0]):
                        result[row - 1][col - 1] = summary // 2
                    else:
                        result[row - 1][col - 1] = summary // 3
                elif col == 1 and col == len(M[0]):
                    if row == 1 or row == len(M):
                        result[row - 1][col - 1] = summary // 2
                    else:
                        result[row - 1][col - 1] = summary // 3
                elif row == 1 or row == len(M):
                    if col == 1 or col == len(M[0]):
                        result[row - 1][col - 1] = summary // 4
                    else:
                        result[row - 1][col - 1] = summary // 6
                elif col == 1 or col == len(M[0]):
                    result[row - 1][col - 1] = summary // 6
                else:
                    result[row - 1][col - 1] = summary // 9

        return result
