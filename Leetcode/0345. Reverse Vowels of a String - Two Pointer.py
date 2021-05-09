# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_converted = list(s)
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while left < right:
            while left < len(s_converted) and s_converted[left] not in vowels:
                left += 1
            while right > left and s_converted[right] not in vowels:
                right -= 1

            if right > left:
                s_converted[left], s_converted[right] = s_converted[right], s_converted[left]
                left += 1
                right -= 1

        return "".join(s_converted)