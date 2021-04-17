# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def __init__(self) -> None:
        self.prebuild = [0] * 1000001
        self.prebuild[1] = 1
        for i in range(2, 1000001):
            if i % 2 == 0:
                self.prebuild[i] = self.prebuild[i // 2] + 1
            else:
                self.prebuild[i] = self.prebuild[i - 1] + 1

    def numberOfSteps(self, num: int) -> int:
        return self.prebuild[num]
