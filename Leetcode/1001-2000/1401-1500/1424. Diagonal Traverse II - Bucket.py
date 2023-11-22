# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        buckets = [[] for _ in range(200001)]
        inMaxLen = True
        col = 0
        while inMaxLen:
            inMaxLen = False
            row = 0
            while row < len(nums):
                if col < len(nums[row]):
                    inMaxLen = True
                    buckets[row + col].append(nums[row][col])
                row += 1
            col += 1
        result = []
        index = 0
        while index < 200001:
            result += buckets[index]
            index += 1
        return result