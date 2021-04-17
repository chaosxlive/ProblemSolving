# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        pattern = [False] * 52
        for c in jewels:
            if 'A' <= c <= 'Z':
                pattern[ord(c) - 65] = True
            else:
                pattern[ord(c) - 97 + 26] = True
        
        result = 0
        for c in stones:
            if ('A' <= c <= 'Z' and pattern[ord(c) - 65]) or ('a' <= c <= 'z' and pattern[ord(c) - 97 + 26]):
                result += 1
        
        return result