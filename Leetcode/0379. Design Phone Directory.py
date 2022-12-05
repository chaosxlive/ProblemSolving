# https://leetcode.com/problems/design-phone-directory/

import heapq


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.availables = [i for i in range(maxNumbers)]
        self.assigned = set()
        heapq.heapify(self.availables)

    def get(self) -> int:
        if len(self.availables) == 0:
            return -1
        num = heapq.heappop(self.availables)
        self.assigned.add(num)
        return num

    def check(self, number: int) -> bool:
        return number not in self.assigned

    def release(self, number: int) -> None:
        if number in self.assigned:
            self.assigned.remove(number)
            heapq.heappush(self.availables, number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
