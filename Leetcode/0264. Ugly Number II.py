# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        index2 = index3 = index5 = 0
        for i in range(1, n):
            nextNum = min(uglyNums[index2] * 2, uglyNums[index3] * 3, uglyNums[index5] * 5)
            if nextNum == uglyNums[index2] * 2:
                index2 += 1
            if nextNum == uglyNums[index3] * 3:
                index3 += 1
            if nextNum == uglyNums[index5] * 5:
                index5 += 1
            uglyNums.append(nextNum)
        return uglyNums[-1]
