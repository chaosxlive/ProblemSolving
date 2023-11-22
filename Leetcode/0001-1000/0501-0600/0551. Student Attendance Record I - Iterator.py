# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        countL = 0
        for c in s:
            if c == 'L':
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0
                if c == 'A':
                    countA += 1
                    if countA > 1:
                        return False
        return True
