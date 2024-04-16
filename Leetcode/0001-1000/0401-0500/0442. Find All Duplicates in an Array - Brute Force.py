# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        seen = set()
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return result
