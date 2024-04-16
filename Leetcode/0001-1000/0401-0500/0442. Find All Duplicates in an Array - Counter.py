# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from collections import Counter
from typing import List


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        return list(map(lambda x: x[0], filter(lambda x: x[1] > 1, Counter(nums).items())))
