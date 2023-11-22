# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
import bisect
from sortedcontainers import SortedList


class TimeMap:

    def __init__(self):
        self.container = defaultdict(SortedList)
        self.values = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        idx = bisect.bisect_right(self.container[key], timestamp)
        if idx < len(self.container[key]) and self.container[key][idx] == timestamp:
            self.values[key][timestamp] = value
        self.container[key].add(timestamp)
        self.values[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.container[key], timestamp) - 1
        return self.values[key][self.container[key][idx]] if idx >= 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
