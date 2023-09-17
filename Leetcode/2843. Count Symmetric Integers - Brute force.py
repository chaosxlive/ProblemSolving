# https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def __init__(self) -> None:
        self.res = set()
        for i in range(11, 100, 11):
            self.res.add(i)
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    for l in range(0, 10):
                        if i + j == k + l:
                            self.res.add(i*1000+j*100+k*10+l)

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return len(list(n for n in range(low, high + 1) if n in self.res))
