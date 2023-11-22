# https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i in range(k + 1):
            result += min(tickets[k], tickets[i])
        for i in range(k + 1, len(tickets)):
            result += min(tickets[k] - 1, tickets[i])
        return result
