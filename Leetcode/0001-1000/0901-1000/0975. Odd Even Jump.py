# https://leetcode.com/problems/odd-even-jump/

from typing import List
from sortedcontainers import SortedList


class Solution:

    def oddEvenJumps(self, arr: List[int]) -> int:
        L = len(arr)
        nextLarges = [-1] * L
        nextLess = [-1] * L
        prevLarges = SortedList([(arr[-1], L - 1)])
        prevLesses = SortedList([(-arr[-1], L - 1)])
        for i in reversed(range(L - 1)):
            n = arr[i]
            j = prevLarges.bisect_left((n, i))
            if j < len(prevLarges):
                nextLarges[i] = prevLarges[j][1]
            prevLarges.add((n, i))
            j = prevLesses.bisect_left((-n, i))
            if j < len(prevLesses):
                nextLess[i] = prevLesses[j][1]
            prevLesses.add((-n, i))
        oddValid = [True] * L
        evenValid = [True] * L
        result = 1
        for i in reversed(range(L - 1)):
            if not (nextLarges[i] == L - 1 or (nextLarges[i] != -1 and evenValid[nextLarges[i]])):
                oddValid[i] = False
            else:
                result += 1
            if not (nextLess[i] == L - 1 or (nextLess[i] != -1 and oddValid[nextLess[i]])):
                evenValid[i] = False
        return result
