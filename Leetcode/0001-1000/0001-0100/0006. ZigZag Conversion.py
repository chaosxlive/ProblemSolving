# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [""] * numRows
        isDirDown = True
        index = 0

        for c in s:
            result[index] += c
            if isDirDown:
                index += 1
            else:
                index -= 1
            if index == numRows - 1:
                isDirDown = False
            elif index == 0:
                isDirDown = True
        
        return "".join(result)