# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, freq in sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[:k]]
