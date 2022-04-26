# https://leetcode.com/problems/print-zero-even-odd/

import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.lockZero = threading.Lock()
        self.lockOdd = threading.Lock()
        self.lockOdd.acquire()
        self.lockEven = threading.Lock()
        self.lockEven.acquire()

        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.lockZero.acquire()
            printNumber(0)
            self.count += 1

            if self.count % 2:
                self.lockOdd.release()
            else:
                self.lockEven.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.lockEven.acquire()
            printNumber(self.count)
            self.lockZero.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.lockOdd.acquire()
            printNumber(self.count)
            self.lockZero.release()