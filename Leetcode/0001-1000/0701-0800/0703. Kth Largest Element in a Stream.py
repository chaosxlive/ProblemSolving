# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from sortedcontainers import SortedList


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.container = SortedList(nums)
        self.target = -k

    def add(self, val: int) -> int:
        self.container.add(val)
        return self.container[self.target]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
