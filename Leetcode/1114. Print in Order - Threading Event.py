# https://leetcode.com/problems/print-in-order/

from threading import Event


class Foo:
    def __init__(self):
        self.event1End = Event()
        self.event2End = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.event1End.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1End.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.event2End.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2End.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
