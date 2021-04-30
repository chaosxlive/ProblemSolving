# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False

        left = 0
        while left < len(arr) and arr[left] < arr[left + 1]:
            left += 1
            
        right = len(arr) - 1
        while right>= 0 and arr[right - 1] > arr[right]:
            right -= 1
        
        return left == right
