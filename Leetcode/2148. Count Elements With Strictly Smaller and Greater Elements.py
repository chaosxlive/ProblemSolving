# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxNum, minNum = max(nums), min(nums)
        return len(list(filter(lambda x: x != maxNum and x != minNum, nums)))
