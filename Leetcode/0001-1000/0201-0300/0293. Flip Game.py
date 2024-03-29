# https://leetcode.com/problems/flip-game/

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        for i in range(len(currentState) - 1):
            if currentState[i] == currentState[i + 1] == '+':
                result.append(currentState[:i] + '--' + currentState[i + 2:])
        return result
