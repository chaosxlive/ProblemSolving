# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = min(income, brackets[0][0]) * brackets[0][1] * 0.01
        income -= min(income, brackets[0][0])
        idx = 1
        while income > 0:
            taxed = min(income, brackets[idx][0] - brackets[idx - 1][0])
            result += taxed * brackets[idx][1] * 0.01
            income -= taxed
            idx += 1
        return result
