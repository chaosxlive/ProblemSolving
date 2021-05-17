# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = 0
        words = sentence.split(' ')
        for index in range(len(words)):
            if len(words[index]) >= len(searchWord) and words[index][:len(searchWord)] == searchWord:
                return index + 1
        return -1
