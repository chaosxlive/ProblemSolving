from typing import List, Optional


class Solution:

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        L = len(bottomLeft)
        result = 0
        for i in range(L - 1):
            iBottom = bottomLeft[i][1]
            iLeft = bottomLeft[i][0]
            iTop = topRight[i][1]
            iRight = topRight[i][0]
            for j in range(i + 1, L):
                jBottom = bottomLeft[j][1]
                jLeft = bottomLeft[j][0]
                jTop = topRight[j][1]
                jRight = topRight[j][0]

                left = max(iLeft, jLeft)
                right = min(iRight, jRight)
                top = min(iTop, jTop)
                bottom = max(iBottom, jBottom)
                if left >= right:
                    continue
                if bottom >= top:
                    continue
                result = max(result, min(right - left, top - bottom)**2)
        return result
