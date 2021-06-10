# https://leetcode.com/problems/diagonal-traverse-ii/

from queue import SimpleQueue


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        next = SimpleQueue()
        next.put((0, 0))
        seen = set()
        seen.add((0, 0))
        result = []
        while not next.empty():
            row, col = next.get()
            result.append(nums[row][col])
            if row + 1 < len(nums) and col < len(nums[row + 1]) and (row + 1, col) not in seen:
                next.put((row + 1, col))
                seen.add((row + 1, col))
            if col + 1 < len(nums[row]) and (row, col + 1) not in seen:
                next.put((row, col + 1))
                seen.add((row, col + 1))
        return result
