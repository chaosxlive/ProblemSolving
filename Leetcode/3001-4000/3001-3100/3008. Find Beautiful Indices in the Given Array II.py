# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

from typing import List


class Solution:

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        if len(s) < len(a) or len(s) < len(b):
            return []

        def find_all(text, pattern):
            pattern = list(pattern)
            sfts = [1] * (len(pattern) + 1)
            sft = 1
            for pos in range(len(pattern)):
                while sft <= pos and pattern[pos] != pattern[pos - sft]:
                    sft += sfts[pos - sft]
                sfts[pos + 1] = sft
            start = 0
            mL = 0
            for c in text:
                while mL == len(pattern) or mL >= 0 and pattern[mL] != c:
                    start += sfts[mL]
                    mL -= sfts[mL]
                mL += 1
                if mL == len(pattern):
                    yield start
            return mL

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
