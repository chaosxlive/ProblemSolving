# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        removed = len(arr) // 20
        return sum(arr[removed:len(arr) - removed]) / (len(arr) - removed * 2)
