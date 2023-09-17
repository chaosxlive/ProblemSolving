# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.used = []

    def popSmallest(self) -> int:
        if len(self.used) == 0:
            self.used.append([1, 1])
            return 1
        if self.used[0][0] != 1:
            if self.used[0][0] == 2:
                self.used[0][0] = 1
            else:
                self.used.insert(0, [1, 1])
            return 1
        ret = self.used[0][1] + 1
        self.used[0][1] += 1
        if len(self.used) > 1 and \
                self.used[0][1] + 1 == self.used[1][0]:
            self.used[0][1] = self.used[1][1]
            del self.used[1]
        return ret

    def addBack(self, num: int) -> None:
        left = 0
        right = len(self.used) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if num > self.used[mid][1]:
                left = mid + 1
            elif num < self.used[mid][0]:
                right = mid - 1
            else:
                if num == self.used[mid][0] and num == self.used[mid][1]:
                    del self.used[mid]
                elif num == self.used[mid][0]:
                    self.used[mid][0] += 1
                elif num == self.used[mid][1]:
                    self.used[mid][1] -= 1
                else:
                    prev = self.used[mid][0]
                    self.used[mid][0] = num + 1
                    self.used.insert(mid, [prev, num - 1])
                break


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
