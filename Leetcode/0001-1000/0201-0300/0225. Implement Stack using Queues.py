# https://leetcode.com/problems/implement-stack-using-queues/

from queue import Queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = Queue(-1)
        self.last = None
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.last = x
        self.container.put(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        length = self.size
        for i in range(length - 1):
            self.last = self.container.get()
            self.container.put(self.last)
        self.size -= 1
        return self.container.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.last

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
