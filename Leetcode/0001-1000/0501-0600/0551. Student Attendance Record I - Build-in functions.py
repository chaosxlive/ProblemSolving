# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count('A') > 1 or s.find('LLL') > -1)
