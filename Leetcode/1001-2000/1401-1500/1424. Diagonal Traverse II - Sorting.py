# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []  # (row + col, row, val)
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                result.append((row + col, -row, nums[row][col]))
        result.sort()
        return list(map(lambda x: x[2], result))
