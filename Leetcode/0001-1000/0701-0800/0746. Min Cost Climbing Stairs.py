# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = [0] * len(cost)
        stairs[0], stairs[1] = cost[0], cost[1]
        for index in range(2, len(cost)):
            stairs[index] = cost[index] + min(stairs[index - 1], stairs[index - 2])
        return min(stairs[-1], stairs[-2])
