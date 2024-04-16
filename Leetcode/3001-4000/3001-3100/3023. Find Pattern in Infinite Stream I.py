# https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    
    # Definition for an infinite stream.
    class InfiniteStream:

        def next(self) -> int:
            pass


class Solution:

    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        checks = []
        i = 0
        while True:
            checks.append([0, i])
            newChecks = []
            n = stream.next()
            for check in checks:
                pi, si = check
                if pi == len(pattern):
                    return si
                if pattern[pi] == n:
                    newChecks.append([pi + 1, si])
            checks = newChecks
            i += 1
