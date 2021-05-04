# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 = index2 = 0
        result = ""
        while index1 < len(word1) and index2 < len(word2):
            result += word1[index1] + word2[index2]
            index1 += 1
            index2 += 1
        if index1 < len(word1):
            result += word1[index1:]
        if index2 < len(word2):
            result += word2[index2:]
        return result
