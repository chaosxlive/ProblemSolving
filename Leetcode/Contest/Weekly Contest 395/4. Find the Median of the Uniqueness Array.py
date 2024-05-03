from collections import defaultdict
from math import inf
from typing import List, Optional


class Solution:

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        L = len(nums)
        total = (1 + L) * L // 2
        medIdx = (total - 1) // 2
        result = inf

        left, right = 0, len(set(nums))
        while left <= right:
            mid = left + (right - left) // 2
            counter = defaultdict(int)
            cnt = 0
            j = 0
            res = 0
            for i, n in enumerate(nums):
                if counter[n] == 0:
                    cnt += 1
                counter[n] += 1
                while cnt > mid:
                    counter[nums[j]] -= 1
                    if counter[nums[j]] == 0:
                        cnt -= 1
                    j += 1
                res += i - j + 1
            if res - 1 >= medIdx:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1
        return result


# print(Solution().medianOfUniquenessArray([1, 2, 3]))
# print(Solution().medianOfUniquenessArray([3, 4, 3, 4, 5]))
# print(Solution().medianOfUniquenessArray([4, 3, 5, 4]))
# print(Solution().medianOfUniquenessArray([46, 73, 46, 46, 46]))  # 1
# print(Solution().medianOfUniquenessArray([88, 68, 68, 88, 68]))  # 2
# print(Solution().medianOfUniquenessArray([52, 31, 92, 52, 52]))  # 2
# print(Solution().medianOfUniquenessArray([99, 73, 14, 84, 14, 73, 14, 14, 14]))  # 2
