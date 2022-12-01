# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        result = 0
        for n in nums:
            if n + diff in s and n + 2 * diff in s:
                result += 1
        return result
