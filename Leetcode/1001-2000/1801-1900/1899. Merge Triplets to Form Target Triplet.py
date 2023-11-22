# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()
        result = [0, 0, 0]
        for triplet in triplets:
            isMatch = True
            for i in range(3):
                if triplet[i] > target[i]:
                    isMatch = False
                    break
            if isMatch:
                for i in range(3):
                    result[i] = max(result[i], triplet[i])
        for i in range(3):
            if result[i] != target[i]:
                return False
        return True
