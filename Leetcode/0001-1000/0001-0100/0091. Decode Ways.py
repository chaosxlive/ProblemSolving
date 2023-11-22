# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        prev1 = prev2 = 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] != '0':
                temp += prev1
            if s[i - 1] == '1' or (s[i - 1] == '2' and '0' <= s[i] <= '6'):
                temp += prev2
            if temp == 0:
                return 0
            prev1, prev2 = temp, prev1
        return prev1
