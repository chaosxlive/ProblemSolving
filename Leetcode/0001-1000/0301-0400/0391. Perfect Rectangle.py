# https://leetcode.com/problems/perfect-rectangle/

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        bottom, top, left, right = 100001, -100001, 100001, -100001
        corners = set()
        areaSum = 0
        for x1, y1, x2, y2 in rectangles:
            areaSum += (x2 - x1) * (y2 - y1)
            bottom = min(bottom, y1)
            top = max(top, y2)
            left = min(left, x1)
            right = max(right, x2)
            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}

        return corners == {(left, bottom), (left, top), (right, bottom), (right, top)} and (top - bottom) * (right - left) == areaSum
