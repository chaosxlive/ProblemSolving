# https://leetcode.com/problems/find-the-maximum-divisibility-score/

from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return sorted(map(lambda d: (-len(list(filter(lambda x: x % d == 0, nums))), d), divisors))[0][1]
