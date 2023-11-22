# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        usedPixel = 0
        for c in s:
            w = widths[ord(c) - 97]
            if usedPixel + w > 100:
                line += 1
                usedPixel = w
            else:
                usedPixel += w
        return [line, usedPixel]
