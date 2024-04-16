# https://leetcode.com/problems/kill-process/

from collections import defaultdict, deque
from typing import List


class Solution:

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        for p, pp in zip(pid, ppid):
            children[pp].append(p)

        dq = deque([kill])
        result = []
        while dq:
            p = dq.popleft()
            result.append(p)
            dq.extend(children[p])
        return result
