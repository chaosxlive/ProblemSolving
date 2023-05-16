# https://leetcode.com/problems/jump-game-iv/

from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        L = len(arr)
        if L <= 1:
            return 0

        indice = defaultdict(list)
        for i, n in enumerate(arr):
            indice[n].append(i)

        q = deque([(0, 0)])
        visited = set([0])

        while q:
            idx, step = q.popleft()
            if idx == L - 1:
                return step
            for nextIdx in indice[arr[idx]]:
                if nextIdx in visited:
                    continue
                visited.add(nextIdx)
                q.append((nextIdx, step + 1))
            indice[arr[idx]].clear()
            if idx - 1 >= 0 and (idx - 1) not in visited:
                visited.add(idx - 1)
                q.append((idx - 1, step + 1))
            if idx + 1 < L and (idx + 1) not in visited:
                visited.add(idx + 1)
                q.append((idx + 1, step + 1))
        return -1
