# https://leetcode.com/problems/decode-ways-ii/

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        prev1, prev2 = (9 if s[0] == '*' else 1), 1
        for i in range(1, len(s)):
            temp = 0

            if s[i] == '*':
                temp += prev1 * 9
            elif s[i] != '0':
                temp += prev1

            if s[i - 1] == '1':
                if '0' <= s[i] <= '9':
                    temp += prev2
                else:
                    temp += prev2 * 9
            elif s[i - 1] == '2':
                if '0' <= s[i] <= '6':
                    temp += prev2
                elif s[i] == '*':
                    temp += prev2 * 6
            elif s[i - 1] == '*':
                if '0' <= s[i] <= '6':
                    temp += prev2 * 2
                elif '7' <= s[i] <= '9':
                    temp += prev2
                else:
                    temp += prev2 * 15
            if temp == 0:
                return 0
            prev1, prev2 = temp % 1000000007, prev1

        return prev1 % 1000000007
