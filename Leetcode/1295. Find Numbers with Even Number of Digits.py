# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if 10 <= num < 100 or 1000 <= num < 10000 or num == 100000:
                result += 1
        return result
