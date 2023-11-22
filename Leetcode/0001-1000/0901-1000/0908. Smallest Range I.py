# https://leetcode.com/problems/smallest-range-i/

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxNum, minNum = 0, 10000
        for num in nums:
            maxNum = max(maxNum, num)
            minNum = min(minNum, num)
        return max(maxNum - minNum - 2 * k, 0)
