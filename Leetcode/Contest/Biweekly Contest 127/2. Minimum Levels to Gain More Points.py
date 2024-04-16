from math import inf
from typing import List, Optional


class Solution:

    def minimumLevels(self, possible: List[int]) -> int:
        S = sum(map(lambda x: 1 if x == 1 else -1, possible))
        HS = S // 2
        d = 0
        # print('>>' + str(S))
        for i, p in enumerate(map(lambda x: 1 if x == 1 else -1, possible[:-1])):
            d += p
            if d > HS:
                return i + 1
        return -1


# print(Solution().minimumLevels([1, 0, 1, 0]))
# print(Solution().minimumLevels([1, 1, 1, 1, 1]))
# print(Solution().minimumLevels([0, 0]))
# print(Solution().minimumLevels([1, 1]))
