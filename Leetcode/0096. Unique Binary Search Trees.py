# https://leetcode.com/problems/unique-binary-search-trees/

from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // factorial(n + 1) // factorial(n)

# https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0