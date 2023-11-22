# https://leetcode.com/problems/make-three-strings-equal/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s1[0] != s3[0]:
            return -1
        minLen = min(len(s1), len(s2), len(s3))
        for i in range(1, minLen):
            if s1[i] != s2[i] or s1[i] != s3[i]:
                minLen = i
                break
        return len(s1) + len(s2) + len(s3) - 3 * minLen
