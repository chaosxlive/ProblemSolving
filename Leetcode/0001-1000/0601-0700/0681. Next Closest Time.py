# https://leetcode.com/problems/next-closest-time/

from itertools import permutations


class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = list(set([int(time[0]), int(time[1]), int(time[3]), int(time[4])])) * 4
        cur = (int(time[0]) * 10 + int(time[1])) * 60 + int(time[3]) * 10 + int(time[4])
        result = 1441
        resultSet = (int(time[0]), int(time[1]), int(time[3]), int(time[4]))
        for n in permutations(nums, 4):
            if 0 <= n[0] * 10 + n[1] < 24 and 0 <= n[2] * 10 + n[3] < 60:
                nt = (n[0] * 10 + n[1]) * 60 + n[2] * 10 + n[3]
                if nt == cur:
                    continue
                if nt < cur:
                    nt += 1440
                if nt - cur < result:
                    result = nt - cur
                    resultSet = n
        return f"{resultSet[0]}{resultSet[1]}:{resultSet[2]}{resultSet[3]}"
