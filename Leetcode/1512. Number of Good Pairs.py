# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        index = [0] * 101
        for n in nums:
            index[n] += 1

        result = 0
        for i in index:
            if i >= 2:
                result += i * (i - 1) // 2

        return result