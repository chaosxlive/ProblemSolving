# https://leetcode.com/problems/array-transformation/

from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        isChanged = False
        newArr = arr[:]
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                newArr[i] -= 1
                isChanged = True
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                newArr[i] += 1
                isChanged = True
        return self.transformArray(newArr) if isChanged else newArr
