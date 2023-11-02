# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps + 1, arrLen)
        result = [0] * arrLen
        result[0] = 1
        for i in range(steps):
            temp = result[:]
            for j in range(arrLen):
                if j > 0:
                    temp[j] += result[j - 1]
                if j < arrLen - 1:
                    temp[j] += result[j + 1]
                temp[j] %= 1000000007
            result = temp
        return result[0]
