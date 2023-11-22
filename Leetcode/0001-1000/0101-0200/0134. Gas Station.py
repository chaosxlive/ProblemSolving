# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        right, left = 0, len(gas) - 1
        require = 0
        current = 0
        while True:
            current += gas[right]
            require += cost[right]
            while left > right and current < require:
                current += gas[left]
                require += cost[left]
                left -= 1
            if current < require:
                return -1
            if left == right and current >= require:
                return (left + 1) % len(gas)
            right += 1
