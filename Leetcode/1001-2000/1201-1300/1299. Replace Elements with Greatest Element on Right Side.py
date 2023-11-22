# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for index in range(len(arr) - 1, -1, -1):
            temp = arr[index]
            arr[index] = maxNum
            if temp > maxNum:
                maxNum = temp
        
        return arr