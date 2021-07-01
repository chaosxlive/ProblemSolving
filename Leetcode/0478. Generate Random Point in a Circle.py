# https://leetcode.com/problems/generate-random-point-in-a-circle/

import random
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        angle = random.uniform(0, 2 * math.pi)
        radius = self.radius * math.sqrt(random.uniform(0, 1))
        return [self.x + radius * math.cos(angle), self.y + radius * math.sin(angle)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
