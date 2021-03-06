# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = result = 0
        for c in s:
            if c == 'R':
                count += 1
            else:
                count -= 1

            if count == 0:
                result += 1
        
        return result