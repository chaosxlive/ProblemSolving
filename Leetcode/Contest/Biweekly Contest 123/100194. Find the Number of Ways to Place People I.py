from typing import List, Optional


class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0
        seen = set()
        for p1 in points:
            for p2 in points:
                p1x, p1y = p1
                p2x, p2y = p2
                if p1x > p2x:
                    p1x, p1y, p2x, p2y = p2x, p2y, p1x, p1y
                elif p1x == p2x and p1y < p2y:
                    p1x, p1y, p2x, p2y = p2x, p2y, p1x, p1y
                if p1x == p2x and p1y == p2y:
                    continue
                if p1y < p2y:
                    continue
                isValid = True
                for p3x, p3y in points:
                    if p3x == p1x and p3y == p1y or p3x == p2x and p3y == p2y:
                        continue
                    if p1x <= p3x <= p2x and p2y <= p3y <= p1y:
                        isValid = False
                        break
                if isValid:
                    if (p1x, p1y, p2x, p2y) not in seen:
                        result += 1
                        seen.add((p1x, p1y, p2x, p2y))
        return result
