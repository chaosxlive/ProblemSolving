# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.result = []

        for candidate in candidates:
            self.backtrack([], 0, candidate)
        
        return self.result

    def backtrack(self, currentPicked: List[int], prevSum:int, currentNum: int):
        currentSum = prevSum + currentNum
        if currentSum > self.target:
            return

        currentPicked.append(currentNum)
        
        if currentSum == self.target:
            self.result.append(currentPicked[:])
            return

        for candidate in self.candidates:
            if candidate < currentNum:
                continue
            self.backtrack(currentPicked[:], currentSum, candidate)
