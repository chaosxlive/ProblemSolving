# https://leetcode.com/problems/maximum-number-of-removable-characters/

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def isSubsequence(s, p, ignored):
            idxS = idxP = 0
            while idxS < len(s):
                if idxS not in ignored:
                    if s[idxS] == p[idxP]:
                        idxP += 1
                if idxP == len(p):
                    return True
                idxS += 1
            return False

        result = 0
        left, right = 0, len(removable)
        while left <= right:
            mid = left + (right - left) // 2
            if isSubsequence(s, p, set(removable[:mid])):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
