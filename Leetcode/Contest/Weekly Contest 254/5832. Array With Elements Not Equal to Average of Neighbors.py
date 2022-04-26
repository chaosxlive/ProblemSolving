# https://leetcode.com/contest/weekly-contest-254/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        index = 0
        while index < len(nums) // 2:
            result.append(nums[index + len(nums) // 2])
            result.append(nums[index])
            index += 1
        if index + len(nums) // 2 < len(nums):
            result.append(nums[index + len(nums) // 2])
        return result
