# https://leetcode.com/problems/building-h2o/

import threading
class H2O:
    def __init__(self):
        self.countH = threading.Semaphore(2)
        self.countO = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        with self.countH:
            self.barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        with self.countO:
            self.barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()