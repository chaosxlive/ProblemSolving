# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1 = ptr2 = 0
        result = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            if firstList[ptr1][1] < secondList[ptr2][0]:
                ptr1 += 1
            elif secondList[ptr2][1] < firstList[ptr1][0]:
                ptr2 += 1
            else:
                result.append([max(firstList[ptr1][0], secondList[ptr2][0]), min(firstList[ptr1][1], secondList[ptr2][1])])
                if firstList[ptr1][1] < secondList[ptr2][1]:
                    ptr1 += 1
                elif secondList[ptr2][1] < firstList[ptr1][1]:
                    ptr2 += 1
                else:
                    ptr1 += 1
                    ptr2 += 1
        return result
