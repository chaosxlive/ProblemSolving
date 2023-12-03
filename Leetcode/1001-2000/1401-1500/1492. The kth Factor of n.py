# https://leetcode.com/problems/the-kth-factor-of-n/

from math import ceil


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        back = []
        cnt = 0
        for i in range(1, ceil(n ** 0.5) + 1):
            if n % i == 0:
                j = n // i
                if i > j:
                    break
                cnt += 1
                if cnt == k:
                    return i
                if i == j:
                    break
                back.append(j)
        print(cnt, back)
        if cnt + len(back) < k:
            return -1
        return back[-(k - cnt)]
