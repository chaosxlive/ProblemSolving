# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.container = [0] * k
        self.size = k
        self.count = 0
        self.ptrOut = 0
        self.ptrIn = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.count += 1
        self.container[self.ptrIn % self.size] = value
        self.ptrIn += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.count -= 1
        self.ptrOut += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.container[self.ptrOut % self.size]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.container[(self.ptrIn - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
