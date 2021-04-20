# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lenS = len(s)
        for i in range(lenS // 2):
            s[i], s[lenS - i - 1] = s[lenS - i - 1], s[i]
