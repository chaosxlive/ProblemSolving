# https://leetcode.com/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        result = (1, 1, 0, 0, 1, 0)
        for i in range(n - 1):
            result = (
                (result[0] + result[4] + result[5]) % 1000000007,
                (result[0] + result[1] + result[2] + result[3] + result[4] + result[5]) % 1000000007,
                (result[1]) % 1000000007,
                (result[2]) % 1000000007,
                (result[0]) % 1000000007,
                (result[4]) % 1000000007,
            )
        return sum(result) % 1000000007
