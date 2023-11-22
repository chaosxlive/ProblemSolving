# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if len(word) >= len(pref):
                if word[:len(pref)] == pref:
                    result += 1
        return result
