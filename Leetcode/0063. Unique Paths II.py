# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        board = [[1 for col in range(len(obstacleGrid[0]))] for row in range(len(obstacleGrid))]

        board[0][0] = 0 if obstacleGrid[0][0] == 1 else 1

        for row in range(1, len(obstacleGrid)):
            board[row][0] = 1 if obstacleGrid[row][0] == 0 and board[row - 1][0] else 0
        for col in range(len(obstacleGrid[0])):
            board[0][col] = 1 if obstacleGrid[0][col] == 0 and board[0][col - 1] else 0

        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    board[row][col] = 0
                else:
                    board[row][col] = board[row - 1][col] + board[row][col - 1]

        return board[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
