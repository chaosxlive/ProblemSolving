from typing import List, Optional

INF = 2147483647


class Solution:

    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        N = len(nums)
        T = len(changeIndices)

        result = T + 1
        left, right = 0, T - 1
        while left <= right:
            mid = left + (right - left) // 2
            tor = mid + 1

            ops = [[] for _ in range(N + 1)]
            for i, cIdx in enumerate(changeIndices[:mid + 1]):
                ops[cIdx].append(i)

            lastIdxs = sorted(((ops[i][-1] if len(ops[i]) > 0 else INF, i) for i in range(1, N + 1)))

            t = 0
            j = 0
            while j < N:
                if nums[lastIdxs[j][1] - 1] == 0:
                    pass
                elif lastIdxs[j][0] == INF:
                    t += nums[lastIdxs[j][1] - 1]
                else:
                    t += 1
                    tor += max(lastIdxs[j][0] - t - 1, 0)
                j += 1

            if t + N <= tor and t <= mid:
                result = min(result, mid + 1)
                right = mid - 1
            else:
                left = mid + 1

        return result if result <= T else -1


print(Solution().earliestSecondToMarkIndices([3, 2, 3], [1, 3, 2, 2, 2, 2, 3]))  # 6
print(Solution().earliestSecondToMarkIndices([0], [1]))  # 1
print(Solution().earliestSecondToMarkIndices([0, 0, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2]))  # 7
print(Solution().earliestSecondToMarkIndices([2, 0, 1], [2, 2, 1, 1]))  # -1
