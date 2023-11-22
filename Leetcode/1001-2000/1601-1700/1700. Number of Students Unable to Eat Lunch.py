# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0 = count1 = 0
        for student in students:
            if student == 0:
                count0 += 1
            else:
                count1 += 1
        index = 0
        while index < len(sandwiches):
            if sandwiches[index] == 0:
                if count0 > 0:
                    count0 -= 1
                else:
                    break
            else:
                if count1 > 0:
                    count1 -= 1
                else:
                    break
            index += 1
        return count0 + count1
