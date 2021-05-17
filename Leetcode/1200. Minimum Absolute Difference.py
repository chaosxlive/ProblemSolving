# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = 2000002
        result = []
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < minDiff:
                minDiff = arr[i] - arr[i - 1]
                result.clear()
                result.append([arr[i - 1], arr[i]])
            elif arr[i] - arr[i - 1] == minDiff:
                result.append([arr[i - 1], arr[i]])
        return result
