# https://leetcode.com/problems/matchsticks-to-square/

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        allLen = sum(matchsticks)
        if allLen == 0 or allLen % 4 != 0:
            return False
        sideLen = allLen // 4

        seen = {}

        def backtrack(matchsticks, sideLen, mask, doneSide):
            total = 0
            for i in range(len(matchsticks) - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[len(matchsticks) - 1 - i]
            if total > 0 and total % sideLen == 0:
                doneSide += 1
                if doneSide == 3:
                    return True
            if (mask, doneSide) in seen:
                return seen[(mask, doneSide)]
            result = False
            rest = sideLen * (total // sideLen + 1) - total
            for i in range(len(matchsticks) - 1, -1, -1):
                if matchsticks[len(matchsticks) - 1 - i] <= rest and mask & (1 << i) != 0:
                    if backtrack(matchsticks, sideLen, mask ^ (1 << i), doneSide):
                        result = True
                        break
            seen[(mask, doneSide)] = result
            return result

        return backtrack(matchsticks, sideLen, (1 << len(matchsticks)) - 1, 0)
