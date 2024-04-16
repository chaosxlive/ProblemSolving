from collections import defaultdict
from functools import reduce
from math import inf
from operator import or_
from typing import List, Optional


class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        if reduce(or_, nums) < k:
            return -1

        res = inf
        left, right = 1, len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            bits = [0] * 31
            i = 0
            isFound = False
            while i < mid - 1:
                n = nums[i]
                j = 0
                while n > 0:
                    bits[j] += n & 1
                    n >>= 1
                    j += 1
                i += 1
            while i < len(nums):
                n = nums[i]
                j = 0
                while n > 0:
                    bits[j] += n & 1
                    n >>= 1
                    j += 1
                c = 0
                for m in reversed(range(31)):
                    c <<= 1
                    if bits[m] > 0:
                        c += 1
                if c >= k:
                    isFound = True
                    break
                n = nums[i - mid + 1]
                j = 0
                while n > 0:
                    bits[j] -= n & 1
                    n >>= 1
                    j += 1
                i += 1
            if isFound:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return -1 if res == inf else res


# print(Solution().minimumSubarrayLength([1, 2, 3], 2))
# print(Solution().minimumSubarrayLength([2, 1, 8], 10))
# print(Solution().minimumSubarrayLength([1, 2], 0))
# print(Solution().minimumSubarrayLength([1, 2], 5))
# print(Solution().minimumSubarrayLength([1, 2, 32, 21], 55))
# print(Solution().minimumSubarrayLength([1] * 100000 + [2], 2))
