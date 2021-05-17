# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        history = {}
        target = len(arr) // 4
        for num in arr:
            if num not in history:
                history[num] = 1
            else:
                history[num] += 1
            if history[num] > target:
                return num
        return -1
