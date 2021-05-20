# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        result = []
        if k > 0:
            for index in range(len(code)):
                codeSum = 0
                for i in range(1, k + 1):
                    codeSum += code[(index + i) % len(code)]
                result.append(codeSum)
        else:
            for index in range(len(code)):
                codeSum = 0
                for i in range(-1, k - 1, -1):
                    codeSum += code[(index + i) % len(code)]
                result.append(codeSum)
        return result