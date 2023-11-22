# https://leetcode.com/problems/high-access-employees/

from typing import List
from collections import defaultdict


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        def pt(t):
            return int(t[:2]) * 60 + int(t[2:])

        dl = defaultdict(list)
        for e, t in access_times:
            dl[e].append(pt(t))
        result = []
        for e, ts in dl.items():
            ts.sort()
            for i in range(2, len(ts)):
                if ts[i - 2] + 60 > ts[i - 1] and ts[i - 2] + 60 > ts[i]:
                    result.append(e)
                    break
        return result
