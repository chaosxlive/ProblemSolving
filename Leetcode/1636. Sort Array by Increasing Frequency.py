# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return [num for num, freq in sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0])) for i in range(freq)]
