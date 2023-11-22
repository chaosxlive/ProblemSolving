# https://leetcode.com/problems/01-matrix/

from queue import Queue


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        nexts = Queue()
        visited = set()
        result = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    nexts.put((row, col, 0))

        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        while not nexts.empty():
            row, col, dist = nexts.get()
            for direction in directions:
                if 0 <= row + direction[0] < len(mat) and 0 <= col + direction[1] < len(mat[0]) and (row + direction[0], col + direction[1]) not in visited:
                    visited.add((row + direction[0], col + direction[1]))
                    nexts.put((row + direction[0], col + direction[1], dist + 1))
                    result[row + direction[0]][col + direction[1]] = dist + 1

        return result
