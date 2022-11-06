# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        if len(nums) % k != 0:
            return False
        counter = Counter(nums)
        cs = sorted(map(lambda x: list(x), counter.items()), key=lambda x: x[0])
        for csi in range(len(cs)):
            n = cs[csi][1]
            if n == 0:
                continue
            for i in range(k):
                if csi + i >= len(cs) or cs[csi + i][0] != cs[csi][0] + i or cs[csi + i][1] < n:
                    return False
                cs[csi + i][1] -= n
        return True
