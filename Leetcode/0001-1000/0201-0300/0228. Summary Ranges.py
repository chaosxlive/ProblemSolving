# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        intervals = [[nums[0], nums[0]]]
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1] + 1:
                intervals[-1][1] = nums[index]
            else:
                intervals.append([nums[index], nums[index]])
            index += 1

        result = []
        for start, end in intervals:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
        return result
