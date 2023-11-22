# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.history = []

    def book(self, start: int, end: int) -> bool:
        indexReplaceStart = indexReplaceEnd = -1
        for index in range(len(self.history)):
            if self.history[index][0] <= start < self.history[index][1] or self.history[index][0] < end < self.history[index][1] or start <= self.history[index][0] < end:
                return False
            if self.history[index][1] == start:
                indexReplaceStart = index
            if self.history[index][0] == end:
                indexReplaceEnd = index
        if indexReplaceStart != -1 and indexReplaceEnd != -1:
            newStart = self.history[indexReplaceStart][0]
            newEnd = self.history[indexReplaceEnd][1]
            if indexReplaceStart > indexReplaceEnd:
                del self.history[indexReplaceStart]
                del self.history[indexReplaceEnd]
            else:
                del self.history[indexReplaceEnd]
                del self.history[indexReplaceStart]
            self.history.append([newStart, newEnd])
        elif indexReplaceStart == -1 and indexReplaceEnd != -1:
            self.history[indexReplaceEnd][0] = start
        elif indexReplaceStart != -1 and indexReplaceEnd == -1:
            self.history[indexReplaceStart][1] = end
        else:
            self.history.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
