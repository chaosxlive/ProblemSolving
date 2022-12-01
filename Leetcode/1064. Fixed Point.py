# https://leetcode.com/problems/fixed-point/

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        result = []
        left, right = 0, len(arr) - 1
        while left <= right:
            center = (left + right) // 2
            if arr[center] < center:
                left = center + 1
            elif arr[center] > center:
                right = center - 1
            else:
                result.append(center)
                right = center - 1
        return -1 if len(result) == 0 else result[-1]
