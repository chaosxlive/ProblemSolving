# https://leetcode.com/problems/similar-rgb-color/

class Solution:
    def __init__(self):
        self.shortHands = list(map(
            lambda x: (int(x, 16), x),
            ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "aa", "bb", "cc", "dd", "ee", "ff"]
        ))

    def similarRGB(self, color: str) -> str:
        return f"#{self.findClosest(color[1:3])}{self.findClosest(color[3:5])}{self.findClosest(color[5:7])}"

    def findClosest(self, color: str):
        c = int(color, 16)
        result = "ZZ"
        dist = 1024
        for (n, s) in self.shortHands:
            if abs(c - n) < dist:
                dist = abs(c - n)
                result = s
        return result
