# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0

        for slideWidth in range(1, len(arr) + 1, 2):
            left, right = 0, len(arr) - 1
            count = 1
            while left < right:
                result += (arr[left] + arr[right]) * count
                left += 1
                right -= 1
                if count < slideWidth and count <= len(arr) - slideWidth:
                    count += 1
            if left == right:
                result += arr[left] * count

        return result
