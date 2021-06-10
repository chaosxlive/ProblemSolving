# https://leetcode.com/contest/weekly-contest-244/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        wasted = [0] * 100001
        counts = [0] * 100001
        count = 0
        wasteSum = 0
        packages.sort()
        iP = 0
        for i in range(1, 100001):
            wasted[i] = wasteSum
            while iP < len(packages) and packages[iP] == i:
                count += 1
                iP += 1
            counts[i] = count
            wasteSum += count

        def tryBox(packages, wasted, counts, box):
            box.sort()
            if box[-1] < packages[-1]:
                return -1
            result = 0
            prev = 0
            for b in box:
                result += (wasted[b] - (wasted[prev] + (b - prev) * counts[prev]))
                prev = b
            return result
            
        result = -1
        for box in boxes:
            temp = tryBox(packages, wasted, counts, box)
            if temp == -1:
                continue
            if result == -1:
                result = temp
            else:
                result = min(result, temp)
        return result % 1000000007 if result != -1 else -1
