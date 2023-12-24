# https://leetcode.com/problems/range-module/

from sortedcontainers import SortedList


class RangeModule:

    def __init__(self):
        self.starts = SortedList()
        self.ends = SortedList()

    def addRange(self, left: int, right: int) -> None:
        self.removeRange(left, right)
        if len(self.starts) == 0:
            self.starts.add(left)
            self.ends.add(right)
            return
        iL = self.ends.bisect_left(left)
        hasL = iL < len(self.starts) and self.ends[iL] == left
        iR = self.starts.bisect_left(right)
        hasR = iR < len(self.starts) and self.starts[iR] == right
        if hasL and hasR:
            left = self.starts[iL]
            right = self.ends[iR]
            self.starts.pop(iR)
            self.ends.pop(iR)
            self.starts.pop(iL)
            self.ends.pop(iL)
            self.starts.add(left)
            self.ends.add(right)
        elif hasL:
            self.ends.pop(iL)
            self.ends.add(right)
        elif hasR:
            self.starts.pop(iR)
            self.starts.add(left)
        else:
            self.starts.add(left)
            self.ends.add(right)

    def queryRange(self, left: int, right: int) -> bool:
        if len(self.starts) == 0:
            return False
        i = self.starts.bisect_right(left)
        if i == 0:
            return False
        i -= 1
        return self.starts[i] <= left and right <= self.ends[i]

    def removeRange(self, left: int, right: int) -> None:
        if len(self.starts) == 0:
            return
        i = self.starts.bisect_right(left)
        if i > 0 and left < self.ends[i - 1]:
            i -= 1
        if i == len(self.starts):
            return
        while i < len(self.starts):
            if left <= self.starts[i]:
                if right >= self.ends[i]:
                    self.starts.pop(i)
                    self.ends.pop(i)
                elif right <= self.starts[i]:
                    break
                else:
                    self.starts.pop(i)
                    self.starts.add(right)
                    break
            else:
                if right >= self.ends[i]:
                    if i + 1 < len(self.starts) and right >= self.starts[i + 1]:
                        self.starts.pop(i + 1)
                        self.ends.pop(i)
                    else:
                        self.ends.pop(i)
                        self.ends.add(left)
                        break
                else:
                    self.starts.add(right)
                    self.ends.add(left)
                    break


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
