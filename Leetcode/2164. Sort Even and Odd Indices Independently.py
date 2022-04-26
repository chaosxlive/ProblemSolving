# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        result = []
        evens = sorted(nums[0::2])
        odds = sorted(nums[1::2], reverse=True)
        index = 0
        while index < len(evens):
            result.append(evens[index])
            if index < len(odds):
                result.append(odds[index])
            index += 1
        return result
