# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (x[1], x[0]), reverse=True)
        result = 0
        for box in boxTypes:
            pickNum = min(truckSize, box[0])
            result += pickNum * box[1]
            truckSize -= pickNum
            if truckSize == 0:
                break
        return result
