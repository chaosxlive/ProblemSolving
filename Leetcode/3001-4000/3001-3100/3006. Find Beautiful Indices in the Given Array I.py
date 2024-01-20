# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

from typing import List


class Solution:

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        if len(s) < len(a) or len(s) < len(b):
            return []

        def find_all(_s, sub):
            start = 0
            while True:
                start = _s.find(sub, start)
                if start == -1:
                    return
                yield start
                start += len(sub)

        ai = list(find_all(s, a))
        bi = list(find_all(s, b))

        left = 0
        result = []
        for idx in ai:
            while left < len(bi) and bi[left] < idx - k:
                left += 1
            if left == len(bi):
                break
            if bi[left] - k <= idx:
                result.append(idx)

        return result
