# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from bisect import bisect_left


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for start, end, prof in jobs:
            index = bisect_left(dp, [start + 1]) - 1
            if dp[index][1] + prof > dp[-1][1]:
                dp.append([end, dp[index][1] + prof])
        return dp[-1][1]
