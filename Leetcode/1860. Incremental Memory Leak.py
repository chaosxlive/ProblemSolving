# https://leetcode.com/problems/incremental-memory-leak/

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        rest1, rest2 = memory1, memory2
        while True:
            if i > rest1 and i > rest2:
                break
            if rest1 >= rest2:
                rest1 -= i
            else:
                rest2 -= i
            i += 1
        return [i, rest1, rest2]
