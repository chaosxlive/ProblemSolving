# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        idx = 0
        prevEmpty = -1
        prevAlly = -1
        result = 0
        while idx < len(forts):
            if forts[idx] == 1:
                if prevEmpty > prevAlly:
                    result = max(result, idx - prevEmpty - 1)
                prevAlly = idx
            elif forts[idx] == -1:
                if prevAlly > prevEmpty:
                    result = max(result, idx - prevAlly - 1)
                prevEmpty = idx
            idx += 1
        return result
