# https://leetcode.com/problems/random-pick-with-weight/

import random


class Solution:

    def __init__(self, w: List[int]):
        self.container = []
        total = sum(w)
        currentSum = 0.0
        for n in w:
            partial = n / total
            self.container.append((currentSum, currentSum + partial))
            currentSum += partial

    def pickIndex(self) -> int:
        pick = random.uniform(0, 1)
        left, right = 0, len(self.container)
        while left < right:
            center = (left + right) // 2
            if self.container[center][0] <= pick < self.container[center][1]:
                return center
            if pick < self.container[center][0]:
                right = center
            else:
                left = center + 1
        return len(self.container) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
