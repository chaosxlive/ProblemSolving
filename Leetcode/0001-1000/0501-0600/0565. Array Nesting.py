# https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        result = 0
        for i in range(len(nums)):
            index = i
            count = 0
            while index not in visited:
                count += 1
                visited.add(index)
                index = nums[index]
            result = max(result, count)
        return result
