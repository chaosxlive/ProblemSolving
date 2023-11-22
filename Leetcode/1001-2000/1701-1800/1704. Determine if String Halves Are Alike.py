# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        vowels = [
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'
        ]

        count = 0
        for c in s[:len(s) // 2]:
            if c in vowels:
                count += 1
        for c in s[len(s) // 2:]:
            if c in vowels:
                count -= 1

        return count == 0
