# https://leetcode.com/problems/reverse-words-in-a-string-ii/

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        prev = ptr = 0
        while True:
            while ptr < len(s) and s[ptr] != ' ':
                ptr += 1

            left = prev
            right = ptr - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            ptr += 1
            prev = ptr

            if ptr >= len(s):
                break
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
