# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {}
        for c in "qwertyuiop":
            keyboard[c] = 1
        for c in "asdfghjkl":
            keyboard[c] = 2
        for c in "zxcvbnm":
            keyboard[c] = 3

        result = []
        for word in words:
            wordLower = word.lower()
            row = keyboard[wordLower[0]]
            isSameRow = True
            for c in wordLower[1:]:
                if keyboard[c] != row:
                    isSameRow = False
                    break
            if isSameRow:
                result.append(word)
        return result
