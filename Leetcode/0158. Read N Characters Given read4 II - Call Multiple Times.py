# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

import queue


class Solution:

    def __init__(self):
        self.container = queue.Queue()
        self.size = 0
        self.isEOF = False

    def read(self, buf: List[str], n: int) -> int:
        buf.clear()
        if self.size >= n:
            for _ in range(n):
                buf.append(self.container.get())
                self.size -= 1
            return n
        while True:
            buf4 = [''] * 4
            cnt = read4(buf4)
            if cnt > 0 and len(buf) < n:
                for char in buf4:
                    if len(char) > 0:
                        self.container.put(char)
                        self.size += 1
            while self.size > 0:
                for _ in range(min(self.size, n - len(buf))):
                    buf.append(self.container.get())
                    self.size -= 1
                if len(buf) == n:
                    break
            if len(buf) == n or cnt == 0:
                break
        return len(buf)
