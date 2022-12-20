# https://leetcode.com/problems/check-array-formation-through-concatenation/

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        indexes = {num: idx for idx, num in enumerate(arr)}
        for piece in pieces:
            if piece[0] not in indexes:
                return False
            for i in range(1, len(piece)):
                if piece[i] not in indexes or indexes[piece[i]] != indexes[piece[i - 1]] + 1:
                    return False
        return True
