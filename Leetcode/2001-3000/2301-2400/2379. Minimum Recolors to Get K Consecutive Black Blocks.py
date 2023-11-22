# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = len(blocks)
        wCnt = blocks[:k - 1].count('W')
        for i in range(len(blocks) - k + 1):
            if blocks[i + k - 1] == 'W':
                wCnt += 1
            result = min(result, wCnt)
            if blocks[i] == 'W':
                wCnt -= 1
        return result
