# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = s + s
        for i in range(len(s)):
            if temp[i:len(s) + i] == goal:
                return True
        return False
