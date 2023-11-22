# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        countTop, countBottom, countSame = [0] * 7, [0] * 7, [0] * 7

        for i in range(len(tops)):
            countTop[tops[i]] += 1
            countBottom[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                countSame[tops[i]] += 1
        
        for i in range(1, 7):
            if countTop[i] + countBottom[i] - countSame[i] >= len(tops):
                return min(countTop[i], countBottom[i]) - countSame[i]

        return -1