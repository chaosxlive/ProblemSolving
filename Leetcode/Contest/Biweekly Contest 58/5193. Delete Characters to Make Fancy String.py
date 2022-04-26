# https://leetcode.com/contest/biweekly-contest-58/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        prev = s[0]
        result = [s[0]]
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                count = 1
            if count < 3:
                result.append(s[i])
        return "".join(result)
