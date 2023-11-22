# https://leetcode.com/problems/additive-number/

from functools import lru_cache


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        @lru_cache(None)
        def dfs(prev1, prev2, idx):
            if idx == len(num):
                return True
            expected = prev1 + prev2
            for l in range(1, len(num) - idx + 1):
                if num[idx] == '0' and l > 1:
                    return False
                v = int(num[idx:idx+l])
                if v < expected:
                    continue
                if v > expected:
                    return False
                if dfs(prev2, v, idx + l):
                    return True
                else:
                    return False
            return False

        for l1 in range(1, len(num)):
            if num[0] == '0' and l1 > 1:
                return False
            num1 = int(num[0:l1])
            for l2 in range(1, len(num) - l1 + 1):
                if num[l1] == '0' and l2 > 1:
                    continue
                if l1 + l2 == len(num):
                    continue
                num2 = int(num[l1:l1 + l2])
                if dfs(num1, num2, l1 + l2):
                    return True
        return False
