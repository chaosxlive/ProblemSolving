# https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
        queens = set((row, col) for row, col in queens)
        result = []
        for iR, iC in directions:
            row, col = king
            while True:
                row += iR
                col += iC
                if 0 <= row < 8 and 0 <= col < 8:
                    if (row, col) in queens:
                        result.append([row, col])
                        break
                else:
                    break
        return result
