# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        left = self.sortArray(nums[:len(nums) // 2])
        right = self.sortArray(nums[len(nums) // 2:])

        indexL = indexR = 0
        result = []
        while indexL < len(left) and indexR < len(right):
            if left[indexL] < right[indexR]:
                result.append(left[indexL])
                indexL += 1
            else:
                result.append(right[indexR])
                indexR += 1

        if indexL < len(left):
            result += left[indexL:]
        if indexR < len(right):
            result += right[indexR:]
        return result
