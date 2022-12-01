# https://leetcode.com/problems/detonate-the-maximum-bombs/

import math


class Bomb:
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.cnt = 1
        self.children = set()


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombMap = {}
        for [x, y, r] in bombs:
            if (x, y) in bombMap:
                bombMap[(x, y)].r = max(r, bombMap[(x, y)].r)
                bombMap[(x, y)].cnt += 1
            else:
                bombMap[(x, y)] = Bomb(x, y, r)
        for i in range(len(bombs) - 1):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]

                dist = math.hypot(x2 - x1, y2 - y1)
                if r1 >= dist:
                    bombMap[(x1, y1)].children.add((x2, y2))
                if r2 >= dist:
                    bombMap[(x2, y2)].children.add((x1, y1))

        seen = set()

        def dfs(x, y):
            if (x, y) in seen:
                return 0
            seen.add((x, y))
            bomb = bombMap[(x, y)]
            cnt = 0
            for [childX, childY] in bomb.children:
                cnt += dfs(childX, childY)
            return cnt + bomb.cnt

        result = 0
        for [x, y] in bombMap.keys():
            seen.clear()
            result = max(result, dfs(x, y))
        return result
