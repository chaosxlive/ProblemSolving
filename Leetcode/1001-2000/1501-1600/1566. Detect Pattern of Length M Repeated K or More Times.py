# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

from typing import List
from collections import Counter


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            pattern = arr[i:i + m]
            if all(arr[i + j * m:i + (j + 1) * m] == pattern for j in range(1, k)):
                return True
        return False
