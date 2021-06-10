# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        seen = set(nums)
        for num in seen:
            if num - 1 not in seen:
                current = num
                count = 1
                while current + 1 in seen:
                    current += 1
                    count += 1
                result = max(result, count)
        return result
