# https://leetcode.com/problems/print-foobar-alternately/

import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = threading.Lock()
        self.lockBar = threading.Lock()
        self.lockBar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lockFoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lockBar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lockBar.acquire()
            printBar()
            self.lockFoo.release()
