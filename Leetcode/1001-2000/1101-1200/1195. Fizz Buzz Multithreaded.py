# https://leetcode.com/problems/fizz-buzz-multithreaded/

from typing import Callable
from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cnt = 1
        self.fizzLock = Lock()
        self.fizzLock.acquire()
        self.buzzLock = Lock()
        self.buzzLock.acquire()
        self.fizzbuzzLock = Lock()
        self.fizzbuzzLock.acquire()
        self.numberLock = Lock()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        # printFizz() outputs "fizz"
        while True:
            if self.fizzLock.acquire(timeout=0.001):
                printFizz()
                self.update()
            if self.cnt > self.n:
                return

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        # printBuzz() outputs "buzz"
        while True:
            if self.buzzLock.acquire(timeout=0.001):
                printBuzz()
                self.update()
            if self.cnt > self.n:
                return

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        # printFizzBuzz() outputs "fizzbuzz"
        while True:
            if self.fizzbuzzLock.acquire(timeout=0.001):
                printFizzBuzz()
                self.update()
            if self.cnt > self.n:
                return

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        # printNumber(x) outputs "x", where x is an integer.
        while True:
            if self.numberLock.acquire(timeout=0.001):
                printNumber(self.cnt)
                self.update()
            if self.cnt > self.n:
                return

    def update(self) -> None:
        self.cnt += 1
        if self.cnt % 15 == 0:
            self.fizzbuzzLock.release()
        elif self.cnt % 5 == 0:
            self.buzzLock.release()
        elif self.cnt % 3 == 0:
            self.fizzLock.release()
        else:
            self.numberLock.release()
