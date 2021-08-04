# https://leetcode.com/problems/permutation-sequence/

from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(list(permutations([str(i) for i in range(1, n + 1)]))[k - 1])
