# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        sns = list(map(int, str(num)))
        maxIdx = len(sns) - 1
        savedIdx = maxIdx
        savedMaxIdx = maxIdx
        for i in reversed(range(len(sns) - 1)):
            if sns[i] > sns[maxIdx]:
                maxIdx = i
            elif sns[i] < sns[maxIdx]:
                savedIdx = i
                savedMaxIdx = maxIdx
        sns[savedIdx], sns[savedMaxIdx] = sns[savedMaxIdx], sns[savedIdx]
        return int(''.join(map(str, sns)))
