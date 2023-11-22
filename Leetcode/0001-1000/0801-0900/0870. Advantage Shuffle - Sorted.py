# https://leetcode.com/problems/advantage-shuffle/

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted([(B[index], index) for index in range(len(B))], key=lambda x: x[0])
        useless = []
        result = [None] * len(sortedA)
        indexA = indexB = 0
        while indexA < len(sortedA) and indexB < len(sortedB):
            while indexA < len(sortedA) and sortedA[indexA] <= sortedB[indexB][0]:
                useless.append(sortedA[indexA])
                indexA += 1
            if indexA >= len(sortedA):
                break
            result[sortedB[indexB][1]] = sortedA[indexA]
            sortedA[indexA] = -1
            indexA += 1
            indexB += 1
        index = 0
        while index < len(result):
            if result[index] == None:
                result[index] = useless.pop()
            index += 1

        return result

