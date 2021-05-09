# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurrence = {}
        index = 0
        while index < len(nums):
            if nums[index] in occurrence and index - occurrence[nums[index]] <= k:
                return True
            occurrence[nums[index]] = index
            index += 1
        return False
