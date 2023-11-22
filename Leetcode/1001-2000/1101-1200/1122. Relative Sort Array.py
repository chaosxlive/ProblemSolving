# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = {}
        for num in arr2:
            counts[num] = 0
        others = []

        for num in arr1:
            if num in counts:
                counts[num] += 1
            else:
                others.append(num)

        result = []
        for num in arr2:
            result += [num] * counts[num]
        result += sorted(others)

        return result
