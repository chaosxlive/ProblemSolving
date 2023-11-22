# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyMap = {}
        for idx, key in enumerate(keyboard):
            keyMap[key] = idx
        finger = 0
        result = 0
        for c in word:
            result += abs(keyMap[c] - finger)
            finger = keyMap[c]
        return result
