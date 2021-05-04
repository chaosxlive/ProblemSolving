# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soliders = []
        for index in range(len(mat)):
            if mat[index][0] == 0:
                soliders.append([0, index])
                continue
            left, right = 0, len(mat[index])
            while left < right - 1:
                center = (left + right) // 2
                if mat[index][center] == 1:
                    left = center
                else:
                    right = center
            soliders.append([left + 1, index])

        return [x[1] for x in sorted(soliders, key=lambda a: a[0])[:k]]
