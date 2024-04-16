from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List, Optional


class Solution:

    def numberOfSubarrays(self, nums: List[int]) -> int:
        NUMS = sorted(map(lambda x: (x[1], x[0]), enumerate(nums)))

        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        cached = defaultdict(int)

        res = 0
        seen = [False] * len(nums)
        for n, i in NUMS:
            seen[i] = True
            r = 1
            if i > 0 and seen[i - 1]:
                if nums[find(i - 1)] == n:
                    r += cached[find(i - 1)]
                union(i - 1, i)
            if i < len(nums) - 1 and seen[i + 1]:
                if nums[find(i + 1)] == n:
                    r += cached[find(i + 1)]
                union(i + 1, i)
            cached[find(i)] = r
            res += r
        return res

        # NUMS = sorted(set(nums), reverse=True)
        # L = len(nums)
        # indexs = defaultdict(list)
        # for i, v in enumerate(nums):
        #     indexs[v].append(i)

        # self.res = 0

        # def solve(maxNIdx, left, right):
        #     if maxNIdx >= len(NUMS):
        #         return
        #     if left > right:
        #         return
        #     N = NUMS[maxNIdx]
        #     idxs = indexs[N]
        #     li = bisect_left(idxs, left)
        #     ri = bisect_right(idxs, right) - 1
        #     if not (0 <= li < len(idxs)) or not (0 <= ri < len(idxs)):
        #         solve(maxNIdx + 1, left, right)
        #         return
        #     if nums[idxs[li]] == N and nums[idxs[ri]] == N:
        #         if ri == li:
        #             self.res += 1
        #         else:
        #             cnt = ri - li + 1
        #             self.res += (1 + cnt) * cnt // 2
        #     if 0 <= left:
        #         solve(maxNIdx + 1, left, idxs[li] - 1)
        #     for i in range(li, ri):
        #         solve(maxNIdx + 1, idxs[i] + 1, idxs[ri] - 1)
        #     if right < L:
        #         solve(maxNIdx + 1, idxs[ri] + 1, right)

        # solve(0, 0, L - 1)
        # return self.res


# a = [1, 2, 3]
# print(bisect_right(a, 2, hi=3))
# print(bisect_left(a, 2, hi=3))

# print(Solution().numberOfSubarrays([1, 4, 3, 3, 2]))
# print(Solution().numberOfSubarrays([4, 33, 2]))  # 3
# print(Solution().numberOfSubarrays([145, 145, 147, 148, 145, 149, 147, 147, 145, 147]))  # 14
