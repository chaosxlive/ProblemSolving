# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        stored = {}
        for index in range(len(arr)):
            if arr[index] not in stored:
                stored[arr[index]] = [index]
            else:
                stored[arr[index]].append(index)
        
        rank = 1
        temp = sorted(stored.items(), key=lambda x: x[0])
        for key, indice in temp:
            for index in indice:
                arr[index] = rank
            rank += 1
        return arr
