# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []

        self.backtrack(sorted(candidates), [], target)

        return self.result


    def backtrack(self, candidates, picked, remain):
        if remain == 0:
            self.result.append(picked[:])
            return

        for i in range(len(candidates)):
            if candidates[i] > remain:
                break

            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            
            self.backtrack(candidates[i + 1:], picked + [candidates[i]], remain - candidates[i])
