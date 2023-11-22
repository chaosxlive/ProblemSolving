# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

import heapq
from collections import defaultdict


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        heap = []
        picked = defaultdict(lambda: 0)
        for rowIdx, row in enumerate(mat):
            heapq.heappush(heap, (row[0], rowIdx, 0))
            picked[row[0]] += 1
        if picked[mat[0][0]] == len(mat):
            return mat[0][0]
        while True:
            droppedNum, rowIdx, droppedColIdx = heapq.heappop(heap)
            if droppedColIdx == len(mat[0]) - 1:
                return -1
            picked[droppedNum] -= 1
            pickedColIdx = droppedColIdx + 1
            pickedNum = mat[rowIdx][pickedColIdx]
            picked[pickedNum] += 1
            if picked[pickedNum] == len(mat):
                return pickedNum
            heapq.heappush(heap, (pickedNum, rowIdx, pickedColIdx))
