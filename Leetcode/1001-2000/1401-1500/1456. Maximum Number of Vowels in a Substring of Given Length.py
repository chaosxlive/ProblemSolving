# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

        count = len(list(filter(lambda x: x, map(isVowel, s[:k]))))
        result = count
        for i in range(k, len(s)):
            if isVowel(s[i-k]):
                count -= 1
            if isVowel(s[i]):
                count += 1
            result = max(result, count)
        return result
