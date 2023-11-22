# https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def findPeak(arr):
            left, right = 0, arr.length()
            while True:
                center = (left + right) // 2
                if arr.get(center - 1) > arr.get(center):
                    right = center
                elif arr.get(center + 1) > arr.get(center):
                    left = center + 1
                else:
                    return center

        def binarySearchLeft(arr, target, left, right):
            while left < right:
                center = (left + right) // 2
                if arr.get(center) > target:
                    right = center
                elif arr.get(center) < target:
                    left = center + 1
                else:
                    return center
            return -1

        def binarySearchRight(arr, target, left, right):
            while left < right:
                center = (left + right) // 2
                if arr.get(center) < target:
                    right = center
                elif arr.get(center) > target:
                    left = center + 1
                else:
                    return center
            return -1

        indexPeak = findPeak(mountain_arr)
        left = binarySearchLeft(mountain_arr, target, 0, indexPeak)
        if left == -1:
            right = binarySearchRight(mountain_arr, target, indexPeak, mountain_arr.length())
            if right == -1:
                return -1
            return right
        return left
