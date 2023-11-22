# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        next = [(matrix[0][0], 0, 0)]
        visited = set()
        count = 0
        visited.add((0, 0))
        while True:
            num, row, col = heapq.heappop(next)
            count += 1
            if count == k:
                return num
            if row + 1 < len(matrix) and (row + 1, col) not in visited:
                heapq.heappush(next, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
            if col + 1 < len(matrix[0]) and (row, col + 1) not in visited:
                heapq.heappush(next, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
