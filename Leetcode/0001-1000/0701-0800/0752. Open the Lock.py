# https://leetcode.com/problems/open-the-lock/

import queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        targetNum = int(target)
        seen = set(map(int, deadends))
        next = queue.Queue()
        next.put((0, 0))

        def getNeighbors(code):
            for i in [1, 10, 100, 1000]:
                digit = (code // i) % 10
                digitUp = (digit + 1) % 10
                digitDown = (digit - 1) % 10
                yield code - digit * i + digitUp * i
                yield code - digit * i + digitDown * i

        while not next.empty():
            code, count = next.get()
            if code == targetNum:
                return count
            for codeNext in getNeighbors(code):
                if codeNext not in seen:
                    seen.add(codeNext)
                    next.put((codeNext, count + 1))
        return -1
