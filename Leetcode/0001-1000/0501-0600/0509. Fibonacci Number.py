# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self) -> None:
        self.fibList = [0, 1, 1]
        for i in range(3, 31):
            self.fibList.append(self.fibList[i - 2] + self.fibList[i - 1])

    def fib(self, n: int) -> int:
        return self.fibList[n]
