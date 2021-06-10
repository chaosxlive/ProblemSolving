# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordChars = [0] * len(words)
        for index in range(len(words)):
            bits = 0
            for c in words[index]:
                bits |= 1 << (ord(c) - 97)
            wordChars[index] = bits

        result = 0
        for i in range(len(wordChars)):
            for j in range(i + 1, len(wordChars)):
                if wordChars[i] & wordChars[j] == 0 and len(words[i]) * len(words[j]) > result:
                    result = len(words[i]) * len(words[j])
        return result
