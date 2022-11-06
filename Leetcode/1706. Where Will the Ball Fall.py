# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        width = len(grid[0])
        rowStatus = [{
            'top': i,
            'bottom': -1
        } for i in range(width)]

        def roll(rowIdx):
            for colIdx in range(width):
                if rowStatus[colIdx]['top'] == -1:
                    continue
                if grid[rowIdx][colIdx] == 1:
                    if colIdx == width - 1:
                        rowStatus[colIdx]['top'] = -1
                        continue
                    if grid[rowIdx][colIdx + 1] == -1:
                        rowStatus[colIdx]['top'] = -1
                        continue
                    rowStatus[colIdx + 1]['bottom'] = rowStatus[colIdx]['top']
                    rowStatus[colIdx]['top'] = -1
                elif grid[rowIdx][colIdx] == -1:
                    if colIdx == 0:
                        rowStatus[colIdx]['top'] = -1
                        continue
                    if grid[rowIdx][colIdx - 1] == 1:
                        rowStatus[colIdx]['top'] = -1
                        continue
                    rowStatus[colIdx - 1]['bottom'] = rowStatus[colIdx]['top']
                    rowStatus[colIdx]['top'] = -1

        def drop():
            for colIdx in range(width):
                rowStatus[colIdx]['top'] = rowStatus[colIdx]['bottom']
                rowStatus[colIdx]['bottom'] = -1

        roll(0)

        for rowIdx in range(1, len(grid)):
            drop()
            roll(rowIdx)

        result = [-1] * width
        for colIdx in range(width):
            if rowStatus[colIdx]['bottom'] != -1:
                result[rowStatus[colIdx]['bottom']] = colIdx
        return result
