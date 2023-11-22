# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        appearence = []
        rest = 26

        for c in sentence:
            if c not in appearence:
                appearence.append(c)
                rest -= 1
                if rest == 0:
                    return True
        
        return False