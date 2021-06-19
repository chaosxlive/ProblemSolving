# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        result = ""
        seen = set()
        for word in words:
            if len(word) == 1:
                if len(result) == 0:
                    result = word
                seen.add(word)
            else:
                if word[:-1] in seen:
                    seen.add(word)
                    if len(word) > len(result):
                        result = word
        return result
