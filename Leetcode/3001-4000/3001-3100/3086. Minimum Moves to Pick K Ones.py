# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

from typing import List


class Solution:

    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        s = ''.join(map(str, nums))
        if '111' in s:
            CONSECUTIVES = 3
        elif '11' in s:
            CONSECUTIVES = 2
        elif '1' in s:
            CONSECUTIVES = 1
        else:
            CONSECUTIVES = 0

        if CONSECUTIVES > k:
            CONSECUTIVES = k
        if maxChanges >= k - CONSECUTIVES:
            return (k - CONSECUTIVES) * 2 + max(0, CONSECUTIVES - 1)

        res = maxChanges * 2
        k -= maxChanges
        ones = [i for i, v in enumerate(nums) if v]
        mid = k // 2
        left = 0
        dist = minDist = sum(abs(i - ones[mid]) for i in ones[:k])
        for right in range(k, len(ones)):
            dist += ones[right] - ones[mid + 1] - (ones[mid] - ones[left])
            distDiff = ones[mid + 1] - ones[mid]
            left += 1
            dist += ((mid + 1 - left) - (right - 1 - mid)) * distDiff
            minDist = min(minDist, dist)
            mid += 1
        res += minDist
        return res
