# https://leetcode.com/problems/maximal-network-rank/

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roadMap = set()
        roadCnt = [0] * n
        for rs, re in roads:
            roadMap.add((min(rs, re), max(rs, re)))
            roadCnt[rs] += 1
            roadCnt[re] += 1
        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                result = max(result, roadCnt[i] + roadCnt[j] - (1 if (i, j) in roadMap else 0))
        return result
