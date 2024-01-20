# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

from typing import List


class Solution:

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        L = len(mat[0])
        for R in mat:
            for c, C in enumerate(R):
                if c & 1:
                    if R[(c + k) % L] != C:
                        return False
                elif R[(c - k) % L] != C:
                    return False
        return True
