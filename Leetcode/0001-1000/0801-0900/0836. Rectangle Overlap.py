# https://leetcode.com/problems/rectangle-overlap/

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Line Check
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        # x1 < x4 && x3 < x2 && y3 < y2 && y1 < y4
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec1[1] < rec2[3]