# https://leetcode.com/problems/two-sum-iii-data-structure-design/

from collections import defaultdict


class TwoSum:

    def __init__(self):
        self.nums = defaultdict(lambda: 0)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        nums = self.nums.keys()
        for num in nums:
            if value - num in self.nums:
                if num + num == value:
                    if self.nums[num] > 1:
                        return True
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
