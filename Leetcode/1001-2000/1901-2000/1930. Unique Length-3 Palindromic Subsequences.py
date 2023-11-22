# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

from collections import defaultdict
import bisect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        history = defaultdict(list)
        for i in range(len(s)):
            history[s[i]].append(i)
        result = 0
        for outer in "abcdefghijklmnopqrstuvwxyz":
            for inner in "abcdefghijklmnopqrstuvwxyz":
                index = bisect.bisect_left(history[outer], 0)
                if index == len(history[outer]):
                    continue
                index = bisect.bisect_left(history[inner], history[outer][index] + 1)
                if index == len(history[inner]):
                    continue
                index = bisect.bisect_left(history[outer], history[inner][index] + 1)
                if index == len(history[outer]):
                    continue
                result += 1
        return result
