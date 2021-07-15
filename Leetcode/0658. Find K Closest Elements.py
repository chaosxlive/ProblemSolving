# https://leetcode.com/problems/find-k-closest-elements/

import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect_left(arr, x)
        left = right - 1
        while k > 0 and left >= 0 and right < len(arr):
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1

        if k > 0:
            if left >= 0:
                left -= k
            else:
                right += k

        return arr[left + 1:right]
