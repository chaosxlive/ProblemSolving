# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = 1
        totalWaitTime = 0

        for customer in customers:
            if customer[0] <= curTime:
                curTime += customer[1]
                totalWaitTime += curTime - customer[0]
            else:
                curTime = customer[0] + customer[1]
                totalWaitTime += customer[1]
        
        return totalWaitTime / len(customers)