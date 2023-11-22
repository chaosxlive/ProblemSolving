# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([char * num for char, num in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)])
