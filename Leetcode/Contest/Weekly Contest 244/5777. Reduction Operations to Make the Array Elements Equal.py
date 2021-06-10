# https://leetcode.com/contest/weekly-contest-244/problems/reduction-operations-to-make-the-array-elements-equal/

from collections import defaultdict


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = defaultdict(lambda: 0)
        for n in nums:
            count[n] += 1
        temp = list(count.items())
        temp.sort()
        result = 0
        for i in range(1, len(temp)):
            result += temp[i][1] * i
        return result
