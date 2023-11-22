# https://leetcode.com/problems/fair-candy-swap/

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice, sumBob = sum(aliceSizes), sum(bobSizes)
        bobCandies = set(bobSizes)
        for c in aliceSizes:
            if c + (sumBob - sumAlice) // 2 in bobCandies:
                return [c, c + (sumBob - sumAlice) // 2]
