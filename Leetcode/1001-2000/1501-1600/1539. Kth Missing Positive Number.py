# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 0
        count = 0
        while index < len(arr):
            if arr[index] != index + count + 1:
                count += 1
                if count == k:
                    return index + count
            else:
                index += 1
        return len(arr) + k
