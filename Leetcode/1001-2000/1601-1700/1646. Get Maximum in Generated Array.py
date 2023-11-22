# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        result = 0
        arr = [0] * (n + 1)
        arr[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                arr[i] = arr[i // 2]
            else:
                arr[i] = arr[i // 2] + arr[i // 2 + 1]
            result = max(result, arr[i])
        return result