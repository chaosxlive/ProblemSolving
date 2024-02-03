# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

from typing import List


class Solution:

    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n

        if abs(x - y) <= 1:
            for step in range(1, n + 1):
                result[step - 1] = (n - step) * 2
            return result

        if y < x:
            x, y = y, x

        LEFT = x - 1
        MID = y - x - 1
        MID_HALF = MID // 2
        RIGHT = n - y
        CYCLE = MID + 2

        for step in range(1, n + 1):
            result[step - 1] += max(0, n - MID - step)

            if CYCLE & 1:
                if step <= CYCLE // 2:
                    result[step - 1] += CYCLE
            else:
                if step < CYCLE // 2:
                    result[step - 1] += CYCLE
                elif step == CYCLE // 2:
                    result[step - 1] += CYCLE // 2

            if MID_HALF > 0 and step > 1:
                result[step - 1] += max(0, LEFT + MID_HALF + 1 - step)
                result[step - 1] -= max(0, LEFT + 1 - step)
                result[step - 1] -= max(0, MID_HALF + 1 - step)
                result[step - 1] += max(0, LEFT + MID_HALF + 2 - step)
                result[step - 1] -= max(0, LEFT + 2 - step)
                result[step - 1] -= max(0, MID_HALF + 2 - step)
                result[step - 1] += max(0, RIGHT + MID_HALF + 1 - step)
                result[step - 1] -= max(0, RIGHT + 1 - step)
                result[step - 1] -= max(0, MID_HALF + 1 - step)
                result[step - 1] += max(0, RIGHT + MID_HALF + 2 - step)
                result[step - 1] -= max(0, RIGHT + 2 - step)
                result[step - 1] -= max(0, MID_HALF + 2 - step)

            if MID & 1 and step >= MID_HALF + 2 and step < MID_HALF + 2 + LEFT:
                result[step - 1] += 1
            if MID & 1 and step >= MID_HALF + 2 and step < MID_HALF + 2 + RIGHT:
                result[step - 1] += 1
        result[0] -= 1
        for i in range(n):
            result[i] *= 2
        return result
