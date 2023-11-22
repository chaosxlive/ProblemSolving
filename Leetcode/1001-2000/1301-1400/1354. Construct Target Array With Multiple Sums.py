# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        curSum = sum(target)
        final = len(target)
        heap = list(map(lambda x: -x, target))
        heapq.heapify(heap)
        while True:
            largest = -heapq.heappop(heap)
            otherSum = curSum - largest
            if otherSum == 1:
                return True
            newElement = largest % otherSum
            if newElement == 0 or largest <= otherSum:
                return False
            heapq.heappush(heap, -newElement)
            curSum = otherSum + newElement
            if curSum == final:
                return True
            elif curSum < final:
                return False
