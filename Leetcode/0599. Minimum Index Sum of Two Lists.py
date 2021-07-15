# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        indice = {}
        indexSum = 3000
        for i in range(len(list1)):
            indice[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in indice:
                if i + indice[list2[i]] < indexSum:
                    indexSum = i + indice[list2[i]]
                    result.clear()
                if i + indice[list2[i]] == indexSum:
                    result.append(list2[i])
        return result
