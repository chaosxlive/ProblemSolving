# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.container = [0] * maxSize
        self.maxSize = maxSize
        self.top = 0

    def push(self, x: int) -> None:
        if self.top == self.maxSize:
            return
        self.container[self.top] = x
        self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            return -1
        self.top -= 1
        return self.container[self.top]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.top, k)):
            self.container[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
