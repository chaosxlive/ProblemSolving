# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnts = [[0, i + 1] for i in range(n)]
        i = 0
        s = k
        while True:
            cnts[i][0] += 1
            if cnts[i][0] == 2:
                break
            i += s
            i %= n
            s += k
        return list(map(lambda x: x[1], filter(lambda x: x[0] == 0, cnts)))
