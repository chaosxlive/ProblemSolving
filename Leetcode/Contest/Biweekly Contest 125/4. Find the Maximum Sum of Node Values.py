from collections import defaultdict
from typing import List, Optional


class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        diffs = sorted(((num ^ k) - num for num in nums), reverse=True)
        s = sum(nums)
        # print(diffs)
        # print(s)
        for i in range(1, len(nums), 2):
            if diffs[i] + diffs[i - 1] > 0:
                s += diffs[i] + diffs[i - 1]
            else:
                break
        return s

        # N = len(nums)
        # neighbors = defaultdict(list)
        # for a, b in edges:
        #     neighbors[a].append(b)
        #     neighbors[b].append(a)
        # S = 0
        # diffs = [0] * N
        # for i, num in enumerate(nums):
        #     S += num
        #     diffs[i] = num ^ k
        # weights = sorted(((diffs[a] + diffs[b], a, b) for a, b in edges), reverse=True)
        # print(S)
        # print(diffs)
        # print(weights)
        # return 0


# print(Solution().maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))
