# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        forceLeft, forceRight = [0] * len(dominoes), [0] * len(dominoes)
        force = 0
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == 'L':
                force = len(dominoes)
            elif dominoes[i] == 'R':
                force = 0
            else:
                force -= 1
            forceLeft[i] = max(force, 0)
        force = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                force = len(dominoes)
            elif dominoes[i] == 'L':
                force = 0
            else:
                force -= 1
            forceRight[i] = max(force, 0)
        result = ['.'] * len(dominoes)
        for i in range(len(dominoes)):
            if forceLeft[i] < forceRight[i]:
                result[i] = 'R'
            elif forceLeft[i] > forceRight[i]:
                result[i] = 'L'
        return "".join(result)
