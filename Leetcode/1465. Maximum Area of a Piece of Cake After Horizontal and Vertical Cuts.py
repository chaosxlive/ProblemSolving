# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        maxH = maxV = 0
        for ih in range(1, len(horizontalCuts)):
            maxH = max(horizontalCuts[ih] - horizontalCuts[ih - 1], maxH)
        for iv in range(1, len(verticalCuts)):
            maxV = max(verticalCuts[iv] - verticalCuts[iv - 1], maxV)
        return (maxH * maxV) % 1000000007
