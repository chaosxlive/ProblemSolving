# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.dp = [[0 for col in range(len(self.candidates) + 1)] for row in range(target + 1)]
        self.dp[0][0] = 1

        backtrackStart = len(self.candidates)

        for index in range(len(self.candidates)):
            if self.candidates[index] > target:
                backtrackStart = index
                break
            col = index + 1
            for row in range(target, self.candidates[index] - 1, -1):
                self.dp[row][col] = max(self.dp[row][col - 1], self.dp[row - self.candidates[index]][col - 1])
            for row in range(self.candidates[index] - 1, -1, -1):
                self.dp[row][col] = self.dp[row][col - 1]

        self.result = []
        self.backtrack(target, backtrackStart, [])

        return self.result

    def backtrack(self, row, col, picked):
        index = col - 1
        if row == 0:
            if picked not in self.result:
                self.result.append(picked[:])
            return
        if row < 0 or self.dp[row][col] == 0:
            return

        self.backtrack(row, col - 1, picked[:])
        self.backtrack(row - self.candidates[index], col - 1, picked[:] + [self.candidates[index]])
