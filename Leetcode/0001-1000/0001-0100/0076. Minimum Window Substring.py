# https://leetcode.com/problems/minimum-window-substring/

from collections import defaultdict, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCounter = defaultdict(deque)
        targetSet = set(t)
        currentCounter = defaultdict(deque)

        for c in t:
            targetCounter[c].append(c)

        def check():
            left, right = 2147483647, -1
            for c in targetSet:
                if len(currentCounter[c]) < len(targetCounter[c]):
                    return False, -1, -1
                while len(currentCounter[c]) > len(targetCounter[c]):
                    currentCounter[c].popleft()
                left = min(left, currentCounter[c][0])
                right = max(right, currentCounter[c][-1])
            return True, left, right

        resultLeft, resultRight = -1, 2147483647
        for i, c in enumerate(s):
            if c in targetSet:
                currentCounter[c].append(i)
                res, left, right = check()
                if res and right - left < resultRight - resultLeft:
                    resultLeft, resultRight = left, right
        return '' if resultLeft == -1 else s[resultLeft:resultRight + 1]
