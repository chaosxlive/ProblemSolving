# https://leetcode.com/problems/most-frequent-even-element/

from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        return (sorted(Counter(filter(lambda x: x % 2 == 0, nums)).items(), key=lambda x: (x[1], -x[0]), reverse=True) or [[-1, 0]])[0][0]
