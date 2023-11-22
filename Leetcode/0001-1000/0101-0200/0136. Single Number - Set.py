# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
            else:
                result.remove(num)
        return list(result)[0]