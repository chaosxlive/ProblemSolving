# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        result = len(word)
        word = 'a' + word
        for i in range(len(word) - 1):
            front, back = word[i], word[i + 1]
            if front != back:
                diff = abs(ord(front) - ord(back))
                result += min(diff, 26 - diff)
        return result
