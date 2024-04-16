# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

from typing import List


class Solution:

    def verifyPreorder(self, preorder: List[int]) -> bool:
        L = len(preorder)
        self.i = 0

        def dfs(lb, ub):
            if self.i == L:
                return True
            n = preorder[self.i]
            if lb > n or n > ub:
                return False
            self.i += 1
            if not dfs(lb, n) and not dfs(n, ub):
                return False
            return True

        return dfs(-2147483648, 2147483647)
