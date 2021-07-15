# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        ptrG = ptrS = 0
        while ptrG < len(g) and ptrS < len(s):
            if g[ptrG] <= s[ptrS]:
                result += 1
                ptrG += 1
                ptrS += 1
            else:
                ptrS += 1
        return result
