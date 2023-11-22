# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        codeSum = []
        currentSum = 0
        for _ in range(3):
            for c in code:
                currentSum += c
                codeSum.append(currentSum)

        result = []
        for i in range(len(code), 2 * len(code)):
            result.append(codeSum[i + k] - codeSum[i] if k > 0 else codeSum[i - 1] - codeSum[i - 1 + k])
        return result
