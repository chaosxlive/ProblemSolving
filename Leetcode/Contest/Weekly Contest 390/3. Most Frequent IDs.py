from collections import Counter, defaultdict
from typing import Optional, List

from sortedcontainers import SortedList


class Solution:

    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        result = [0] * len(nums)

        s = SortedList()
        fs = defaultdict(int)

        for i, [n, f] in enumerate(zip(nums, freq)):
            s.discard(fs[n])
            fs[n] += f
            s.add(fs[n])
            result[i] = s[-1]

        return result

        # result = [0] * len(nums)
        # counter = Counter()
        # for i, [n, f] in enumerate(zip(nums, freq)):
        #     counter[n] += f
        #     result[i] = counter.most_common(1)[0][1]
        # return result
