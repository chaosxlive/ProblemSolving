# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        while True:
            center = (left + right) // 2
            if arr[center - 1] > arr[center]:
                right = center
            elif arr[center + 1] > arr[center]:
                left = center + 1
            else:
                return center
        