# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        dif = 1
        bestDif = 3
        hasSix = False
        temp = num
        while temp > 0:
            if temp % 10 == 6:
                hasSix = True
                bestDif = 3 * dif
            dif *= 10
            temp //= 10
        
        if hasSix:
            return num + bestDif
        else:
            return num
