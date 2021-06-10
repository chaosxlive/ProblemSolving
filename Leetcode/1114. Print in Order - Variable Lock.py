# https://leetcode.com/problems/print-in-order/

class Foo:
    def __init__(self):
        self.count = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.count += 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.count < 2:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.count += 1

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.count < 3:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
