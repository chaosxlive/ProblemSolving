# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

from functools import lru_cache
from typing import List

INF = 2147483647


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if (len(jobDifficulty) < d):
            return -1

        @lru_cache(None)
        def solve(jobIdx: int, day: int):
            if day == d:
                return 0
            result = INF
            jobCnt = len(jobDifficulty) - jobIdx if day == d - 1 else 1
            m = max(jobDifficulty[jobIdx:jobIdx+jobCnt])
            while jobCnt < len(jobDifficulty) - jobIdx - d + day + 2:
                m = max(m, jobDifficulty[jobIdx+jobCnt-1])
                s = solve(jobIdx + jobCnt, day + 1)
                result = min(result, m + s)
                jobCnt += 1
            return result

        return solve(0, 0)
