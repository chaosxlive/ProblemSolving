# https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        cnt = 0
        for i, c in enumerate(s):
            if c == '0':
                result += i - cnt
                cnt += 1
        return result
