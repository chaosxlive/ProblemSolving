# https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        seenRev = {w[::-1]: i for i, w in enumerate(words)}
        result = []
        for index, word in enumerate(words):
            wordRev = word[::-1]
            if word in seenRev and seenRev[word] != index:
                result.append([index, seenRev[word]])
            for i in range(0, len(word)):
                if word[:-i - 1] in seenRev and word[-i - 1:] == wordRev[:i + 1]:
                    result.append([index, seenRev[word[:-i - 1]]])
                if word[i + 1:] in seenRev and word[:i + 1] == wordRev[-i - 1:]:
                    result.append([seenRev[word[i + 1:]], index])
        return result
