# https://leetcode.com/problems/find-the-index-of-the-large-integer/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l = reader.length()
        left, right = 0, l
        while True:
            rest = right - left
            if rest == 1:
                return left
            half = rest // 2 + left
            if rest % 2 == 1:
                result = reader.compareSub(left, half - 1, half + 1, right - 1)
                if result > 0:
                    right = half
                elif result < 0:
                    left = half + 1
                else:
                    return half
            else:
                result = reader.compareSub(left, half - 1, half, right - 1)
                if result > 0:
                    right = half
                else:
                    left = half
