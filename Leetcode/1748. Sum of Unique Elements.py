# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        result = 0
        for key in count.keys():
            if count[key] == 1:
                result += key
        return result