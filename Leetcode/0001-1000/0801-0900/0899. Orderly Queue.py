# https://leetcode.com/problems/orderly-queue/

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ms = s + s
            l = len(s)
            result = s
            for i in range(l):
                result = min(result, ms[i:i + l])
            return result
        return ''.join(sorted(s))
