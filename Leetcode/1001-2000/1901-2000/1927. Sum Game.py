# https://leetcode.com/problems/sum-game/

class Solution:
    def sumGame(self, num: str) -> bool:
        unknownLeft = unknownRight = 0
        sumLeft = sumRight = 0
        for i in range(len(num) // 2):
            if num[i] == '?':
                unknownLeft += 1
            else:
                sumLeft += int(num[i])
        for i in range(len(num) // 2, len(num)):
            if num[i] == '?':
                unknownRight += 1
            else:
                sumRight += int(num[i])

        if unknownLeft == unknownRight:
            return sumLeft != sumRight

        if unknownLeft > unknownRight:
            unknown = unknownLeft - unknownRight
            diff = sumLeft - sumRight
        else:
            unknown = unknownRight - unknownLeft
            diff = sumRight - sumLeft
        return (unknown + 1) // 2 * 9 + diff > 0 or unknown // 2 * 9 + diff < 0
