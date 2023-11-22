# https://leetcode.com/problems/three-equal-parts/

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        prefixSum = [0] * len(arr)
        for i in range(len(arr)):
            prefixSum[i] = (prefixSum[i - 1] << 1) + arr[i]
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                a = prefixSum[i]
                b = prefixSum[j] - (prefixSum[i] << (j - i))
                c = prefixSum[-1] - (prefixSum[j] << (len(arr) - 1 - j))
                if a == b == c:
                    return [i, j + 1]
        return [-1, -1]

# TLE