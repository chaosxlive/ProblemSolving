# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10000
        isLast = False
        while True:
            if right - left == 1:
                isLast = True
            center = (left + right) // 2
            num = reader.get(center)
            if num == 2147483647 or target < num:
                right = center
            elif target > num:
                left = center
            else:
                return center
            if isLast:
                return -1
