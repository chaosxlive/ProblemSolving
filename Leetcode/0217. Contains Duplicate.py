# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurrence = set()
        for num in nums:
            if num in occurrence:
                return True
            occurrence.add(num)
        return False