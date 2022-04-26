# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])
