# https://leetcode.com/problems/poor-pigs/

import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log10(buckets) / math.log10(minutesToTest // minutesToDie + 1))
