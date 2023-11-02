# https://leetcode.com/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        while mainTank >= 5 and additionalTank > 0:
            transfered = min(mainTank // 5, additionalTank)
            result += 10 * transfered * 5
            mainTank -= 4 * transfered
            additionalTank -= transfered
        result += mainTank * 10
        return result
