# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.prebuild = [0, 1, 2]
        for i in range(3, 46):
            self.prebuild.append(self.prebuild[i - 2] + self.prebuild[i - 1])

    def climbStairs(self, n: int) -> int:
        return self.prebuild[n]