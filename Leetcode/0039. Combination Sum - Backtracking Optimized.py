# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.candidates = sorted(candidates)
        self.backtrack(target, [], 0)

        return self.result

    def backtrack(self, remain, currentPicked, startIndex):
        if remain == 0:
            self.result.append(currentPicked[:])
            return
        for i in range(startIndex, len(self.candidates)):
            if self.candidates[i] > remain:
                break
            self.backtrack(remain - self.candidates[i], currentPicked + [self.candidates[i]], i)
        