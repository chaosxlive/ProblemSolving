# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numMap = {}
        for idx, num in enumerate(nums):
            numMap[num] = idx

        for origin, replaced in operations:
            numMap[replaced] = numMap[origin]
            del numMap[origin]

        return list(map(lambda x: x[1], sorted(map(lambda x: (x[1], x[0]), numMap.items()))))
