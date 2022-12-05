# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def getCount(word):
            result = [0] * 26
            for c in word:
                result[ord(c) - 97] += 1
            return result

        result = 0
        target = getCount(chars)
        for word in words:
            wCount = getCount(word)
            if all(wCount[i] <= target[i] for i in range(26)):
                result += len(word)
        return result
