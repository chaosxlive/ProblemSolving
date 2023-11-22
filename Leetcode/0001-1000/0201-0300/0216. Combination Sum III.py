# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.count = k
        self.result = []
        self.dfs(1, [], 0, n)
        return self.result

    def dfs(self, currentNum, picked, count, remain):
        if count == self.count and remain == 0:
            self.result.append(picked[:])
            return

        if currentNum > 9 or count > self.count or remain < 0:
            return

        self.dfs(currentNum + 1, picked + [currentNum], count + 1, remain - currentNum)
        self.dfs(currentNum + 1, picked, count, remain)