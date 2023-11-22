# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        length = len(startTime)
        index = 0
        result = 0
        while index < length:
            if startTime[index] <= queryTime <= endTime[index]:
                result += 1
            index += 1
        return result
