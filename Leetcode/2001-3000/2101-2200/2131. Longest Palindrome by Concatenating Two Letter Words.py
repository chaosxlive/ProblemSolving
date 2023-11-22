# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result = 0
        palindromeCnt = 0
        package = defaultdict(lambda: 0)
        for word in words:
            isPalindrome = word[0] == word[1]
            flipped = f"{word[1]}{word[0]}"
            if package[flipped] > 0:
                result += 4
                package[flipped] -= 1
                if isPalindrome:
                    palindromeCnt -= 1
            else:
                package[word] += 1
                if isPalindrome:
                    palindromeCnt += 1
        return result + (2 if palindromeCnt > 0 else 0)
