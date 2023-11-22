# https://leetcode.com/problems/last-visited-integers/

from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        arr = []
        idx = -1
        result = []

        for word in words:
            if word == 'prev':
                if idx == -1:
                    result.append(-1)
                else:
                    result.append(arr[idx])
                    idx -= 1
            else:
                arr.append(int(word))
                idx = len(arr) - 1
        return result
