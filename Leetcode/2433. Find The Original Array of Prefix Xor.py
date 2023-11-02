# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [pref[0]] * len(pref)
        for i in range(1, len(pref)):
            result[i] = pref[i] ^ pref[i - 1]
        return result
