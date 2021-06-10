# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordChars = [[] for _ in range(len(words))]
        for index in range(len(words)):
            wordChars[index].append(len(words[index]))
            wordChars[index].append(set(words[index]))

        result = 0
        for i in range(len(wordChars)):
            for j in range(i + 1, len(wordChars)):
                if wordChars[i][0] * wordChars[j][0] > result and len(wordChars[i][1].union(wordChars[j][1])) == len(wordChars[i][1]) + len(wordChars[j][1]):
                    result = wordChars[i][0] * wordChars[j][0]
        return result
