# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sList = list(s)
        left, right = 0, len(sList) - 1
        while True:
            while left < len(sList) and not sList[left].isalpha():
                left += 1
            if left >= len(sList):
                break
            while right >= 0 and not sList[right].isalpha():
                right -= 1
            if right < 0:
                break
            if left >= right:
                break
            sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1
            if left >= right:
                break
        return ''.join(sList)
