# https://leetcode.com/contest/weekly-contest-242/problems/jump-game-vii/

import queue


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queueJump = queue.SimpleQueue()
        queueJump.put(0)
        indexLast = 0
        while not queueJump.empty():
            start = queueJump.get()
            for i in range(max(start + minJump, indexLast), min(start + maxJump + 1, len(s))):
                if s[i] == '0':
                    if i == len(s) - 1:
                        return True
                    queueJump.put(i)
            indexLast = min(start + maxJump + 1, len(s))
        return False
