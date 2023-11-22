# https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [0] * 10

        def getRodData(code):
            return (0 if code[0] == 'R' else 1 if code[0] == 'G' else 2), int(code[1])

        for i in range(0, len(rings), 2):
            color, n = getRodData(rings[i:i + 2])
            rods[n] |= 1 << color

        result = 0
        for rod in rods:
            if rod == 7:
                result += 1
        return result
