# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            temp = 0
            for wealth in account:
                temp += wealth
            if temp > maxWealth:
                maxWealth = temp
        
        return maxWealth