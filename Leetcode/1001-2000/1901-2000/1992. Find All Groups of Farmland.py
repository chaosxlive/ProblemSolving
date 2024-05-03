# https://leetcode.com/problems/find-all-groups-of-farmland/

from typing import List


class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    m = i + 1
                    while m < len(land) and land[m][j] == 1:
                        m += 1
                    n = j + 1
                    while n < len(land[i]) and land[i][n] == 1:
                        n += 1
                    res.append([i, j, m - 1, n - 1])
        return res
