import math
from typing import List, Optional


class Solution:

    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        L = len(nums)
        if nums.count(1) == 0:
            return 2 * k
        if k == 1:
            return 0
        if L == 2:
            if nums[0] + nums[1] == 1:
                return 2 * (k - 1)
            return 2 * (k - 2) + 1
        # if k == 2:
        #     for i in range(1, len(nums)):
        #         if nums[i] == 1 and nums[i - 1] == 1:
        #             return 1
        #     return 2
        # if k == 3:
        #     for i in range(2, len(nums)):
        #         if nums[i - 2] == 1 and nums[i - 1] == 1 and nums[i] == 1:
        #             return 2
        #     for i in range(1, len(nums)):
        #         if nums[i] == 1 and nums[i - 1] == 1:
        #             return 3
        #     return 4

        # if k - 1 <= maxChanges:
        #     for i in range(2, len(nums)):
        #         if nums[i - 2] == 1 and nums[i - 1] == 1 and nums[i] == 1:
        #             return 2

        result = math.inf
        left, right = 0, min(k, maxChanges)
        while left <= right:
            mid = left + (right - left) // 2
            target = k - mid
            cnt = 0
            l = 0
            r = -1
            dist = 0
            while r < L - 1 and cnt < target - 1:
                r += 1
                dist += cnt
                if nums[r] == 1:
                    cnt += 1
            if cnt != target - 1:
                left = mid + 1
                continue
            r += 1
            isFound = False
            while r < L:
                dist += cnt
                if nums[r] == 1:
                    result = min(result, dist + 2 * mid)
                    isFound = True
                    while l <= r:
                        dist -= cnt
                        if nums[l] == 1:
                            cnt -= 1
                            break
                r += 1
            if isFound:
                left = mid + 1
            else:
                right = mid - 1

        return result


print(Solution().minimumMoves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1))  # 3
# print(Solution().minimumMoves([1, 1, 1, 0, 0, 1, 1, 0, 0, 1], 3, 1))  # 2
# print(Solution().minimumMoves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 4, 1))  # ?
# print(Solution().minimumMoves([0, 0, 0, 0], 2, 3))  # 4
# print(Solution().minimumMoves([0, 0, 1, 0], 2, 3))  # 2
# print(Solution().minimumMoves([1, 1], 2, 2))  # 1
