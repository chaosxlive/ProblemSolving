# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

from math import inf, lcm
from typing import List


class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        L = len(coins)
        MAX = max(coins)
        left, right = 1, MAX * k
        res = inf
        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            for mask in range(1, 1 << L):
                idxs = []
                i = 0
                while mask > 0:
                    if mask & 1 > 0:
                        idxs.append(i)
                    mask >>= 1
                    i += 1
                if len(idxs) % 2 == 1:
                    cnt += mid // lcm(*map(lambda x: coins[x], idxs))
                else:
                    cnt -= mid // lcm(*map(lambda x: coins[x], idxs))
            if cnt > k:
                right = mid - 1
            elif cnt < k:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1
        return res
