# https://leetcode.com/problems/naming-a-company/

from typing import List
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        seen = defaultdict(set)
        for idea in ideas:
            seen[idea[0]].add(idea[1:])
        result = 0
        for ideaA, setA in seen.items():
            for ideaB, setB in seen.items():
                if ideaA >= ideaB:
                    continue
                intersectCnt = len(setA & setB)
                result += (len(setA) - intersectCnt) * (len(setB) - intersectCnt)
        return result * 2
