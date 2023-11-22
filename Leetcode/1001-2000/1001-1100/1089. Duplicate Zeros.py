# https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        countZero = 0
        while index < len(arr) - countZero:
            if arr[index] == 0:
                countZero += 1
            index += 1
        
        ptrRead = len(arr) - 1 - countZero
        ptrWrite = len(arr) - 1

        if index > len(arr) - countZero:
            arr[ptrWrite] = 0
            ptrWrite -= 1

        while ptrRead >= 0:
            if arr[ptrRead] == 0:
                arr[ptrWrite] = 0
                arr[ptrWrite - 1] = 0
                ptrWrite -= 2
            else:
                arr[ptrWrite] = arr[ptrRead]
                ptrWrite -= 1
            ptrRead -= 1
        
