# https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefixMasks = [0] * 1024
        prefixMasks[0] = 1
        result = 0
        mask = 0
        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            result += prefixMasks[mask]
            for b in range(10):
                result += prefixMasks[mask ^ 1 << b]
            prefixMasks[mask] += 1
        return result
