from functools import lru_cache
from itertools import accumulate
from typing import List, Optional


class Solution:

    def maximumStrength(self, nums: List[int], k: int) -> int:
        acc = [0, *accumulate(nums)]
        L = len(nums)

        @lru_cache(None)
        def solve(i, rest):
            if rest == 0:
                return 0, 0
            MAX = float('-inf')
            MIN = float('inf')
            # print(L - i + 1, L - rest + 1)
            for l in range(1, min(L - i + 1, L - rest + 2)):
                # print(i, l)
                s = acc[i + l] - acc[i]
                MAX = max(MAX, s * rest - solve(i + l, rest - 1)[1])
                MIN = min(MIN, s * rest - solve(i + l, rest - 1)[0])
            # print(f'{i=} {rest=}: {MAX=}; {MIN=}')
            return MAX, MIN

        return max(solve(i, k)[0] for i in range(L - k + 1))


# print(Solution().maximumStrength([1, 2, 3, -1, 2], 3))
# print(Solution().maximumStrength([-1, -2, -3], 1))
# print(Solution().maximumStrength([-99, 85], 1))  # 85
# print(Solution().maximumStrength([7, 62], 1))  # 69
# print(Solution().maximumStrength([-1000000000,-100000000,-10000000,123,234],5))  # -4630000012
