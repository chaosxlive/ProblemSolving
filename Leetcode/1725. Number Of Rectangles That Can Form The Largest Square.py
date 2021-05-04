# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLength = 0
        maxCount = 0

        for rectangle in rectangles:
            square = min(rectangle[0], rectangle[1])
            if square > maxLength:
                maxLength = square
                maxCount = 1
            elif square == maxLength:
                maxCount += 1
            
        return maxCount