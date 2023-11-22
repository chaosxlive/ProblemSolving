# https://leetcode.com/problems/course-schedule-ii/

from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requiredCourseCnt = [0] * numCourses
        nextCourse = defaultdict(list)
        for courseAfter, courseBefore in prerequisites:
            requiredCourseCnt[courseAfter] += 1
            nextCourse[courseBefore].append(courseAfter)
        result = []
        pickedCourse = set(map(lambda x: x[0],filter(lambda x: x[1] == 0, enumerate(requiredCourseCnt))))
        q = deque(pickedCourse)
        while q:
            courseId = q.popleft()
            result.append(courseId)
            for nextCourseId in nextCourse[courseId]:
                requiredCourseCnt[nextCourseId] -= 1
                if requiredCourseCnt[nextCourseId] == 0 and nextCourseId not in pickedCourse:
                    q.append(nextCourseId)
                    pickedCourse.add(nextCourseId)
        if len(pickedCourse) < numCourses:
            return []
        return result