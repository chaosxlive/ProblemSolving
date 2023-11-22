# https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        vSeen = set()
        
        for first in range(len(word)):
            if word[first] in 'aeiou':
                vSeen.add(word[first])
                for last in range(first + 1, len(word)):
                    if word[last] in 'aeiou':
                        vSeen.add(word[last])
                    else:
                        break

                    if len(vSeen) == 5:
                        result += 1
            vSeen.clear()

        return result
