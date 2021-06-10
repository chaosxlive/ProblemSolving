# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.history = []
        self.currentIndex = -1
        self.latestIndex = -1
        self.latestTime = -5000

    def ping(self, t: int) -> int:
        self.currentIndex += 1
        self.history.append(t)
        while t - self.latestTime > 3000 and self.latestIndex < self.currentIndex:
            self.latestIndex += 1
            self.latestTime = self.history[self.latestIndex]
        return self.currentIndex - self.latestIndex + 1

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
