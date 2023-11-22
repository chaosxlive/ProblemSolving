# https://leetcode.com/problems/shortest-way-to-form-string/

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        indice = [[-1] * 26 for _ in range(len(source) + 1)]
        for ir, c in enumerate(reversed(source)):
            i = len(source) - ir - 1
            for j in range(26):
                indice[i][j] = indice[i + 1][j]
            indice[i][ord(c) - 97] = i
        result = 0
        idx = 0
        while idx < len(target):
            result += 1
            ci = ord(target[idx]) - 97
            row = 0
            if indice[row][ci] == -1:
                return -1
            row = indice[row][ci] + 1
            idx += 1
            while row < len(source) and idx < len(target):
                ci = ord(target[idx]) - 97
                if indice[row][ci] == -1:
                    break
                row = indice[row][ci] + 1
                idx += 1

        return result
