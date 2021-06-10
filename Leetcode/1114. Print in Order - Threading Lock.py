# https://leetcode.com/problems/print-in-order/

from threading import Lock


class Foo:
    def __init__(self):
        self.lock2 = Lock()
        self.lock2.acquire()
        self.lock3 = Lock()
        self.lock3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock2.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
