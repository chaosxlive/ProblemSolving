# https://leetcode.com/problems/maximum-number-of-books-you-can-take/

from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:

        def rangeSum(left, right):
            cnt = min(books[right], right - left + 1)
            return (2 * books[right] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * len(books)

        for i in range(len(books)):
            while len(stack) > 0 and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            if len(stack) == 0:
                dp[i] = rangeSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + rangeSum(j + 1, i)
            stack.append(i)
        return max(dp)
