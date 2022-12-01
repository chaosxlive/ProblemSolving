# https://leetcode.com/problems/student-attendance-record-ii/

class Solution:

    def __init__(self):
        # Safe, Has A, Has A and 1 L end, Has A and 2 L end, 1 L end, 2 L end
        self.results = [(0, 0, 0, 0, 0, 0), (1, 1, 0, 0, 1, 0)]
        self.calculated = 0

    def checkRecord(self, n: int) -> int:
        if n > self.calculated:
            self.genToN(n)
        return sum(self.results[n]) % 1000000007

    def genNext(self):
        last = self.results[-1]
        self.results.append((
            (last[0] + last[4] + last[5]) % 1000000007,
            (last[0] + last[1] + last[2] + last[3] + last[4] + last[5]) % 1000000007,
            (last[1]) % 1000000007,
            (last[2]) % 1000000007,
            (last[0]) % 1000000007,
            (last[4]) % 1000000007,
        ))
        self.calculated += 1

    def genToN(self, n):
        while self.calculated < n:
            self.genNext()
