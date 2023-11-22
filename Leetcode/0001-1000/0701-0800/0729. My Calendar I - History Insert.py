# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.history = []

    def book(self, start: int, end: int) -> bool:
        for h in self.history:
            if h[0] <= start < h[1] or h[0] < end < h[1] or start <= h[0] < end:
                return False
        self.history.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
