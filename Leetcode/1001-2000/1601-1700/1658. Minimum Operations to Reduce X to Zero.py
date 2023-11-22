# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

from typing import List
from itertools import accumulate


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        acc = [0] + list(accumulate(nums))
        left, right = 0, 1
        result = 2147483647
        while True:
            diff = acc[right] - acc[left]
            rest = acc[-1] - diff
            if rest == x:
                result = min(result, len(acc) - (right - left + 1))
                right += 1
                left += 1
            elif rest < x:
                left += 1
                if left == right:
                    right += 1
            else:
                right += 1
            if right >= len(acc):
                break
        return result if result != 2147483647 else len(nums) if acc[-1] == x else -1
