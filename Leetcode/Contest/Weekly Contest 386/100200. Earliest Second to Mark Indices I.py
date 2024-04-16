from typing import List, Optional


class Solution:

    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        N = len(nums)
        T = len(changeIndices)

        result = T + 1
        left, right = 0, T - 1
        while left <= right:
            mid = left + (right - left) // 2

            ops = [[] for _ in range(N + 1)]
            for i, cIdx in enumerate(changeIndices[:mid + 1]):
                ops[cIdx].append(i)

            isValid = True

            for i in range(1, N + 1):
                if len(ops[i]) == 0:
                    isValid = False
                    break

            if isValid:
                lastIdxs = sorted(((ops[i][-1], i) for i in range(1, N + 1)))

                t = 0
                j = 0
                while j < N:
                    t += nums[lastIdxs[j][1] - 1]
                    if t > lastIdxs[j][0]:
                        isValid = False
                        break
                    t += 1
                    j += 1

            if isValid:
                result = mid + 1
                right = mid - 1
            else:
                left = mid + 1

        return -1 if result == T + 1 else result


# [1,1]
# [1,2,1,1,1,1,1,1,2]
# 4

# print(Solution().earliestSecondToMarkIndices([2, 2, 0], [2, 2, 2, 2, 3, 2, 2, 1]))  # 8
# print(Solution().earliestSecondToMarkIndices([1, 3], [1, 1, 1, 2, 1, 1, 1]))  # 6
# print(Solution().earliestSecondToMarkIndices([0, 1], [2, 2, 2]))  # -1
# print(Solution().earliestSecondToMarkIndices([1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 2]))  # 4
