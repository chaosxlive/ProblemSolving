# https://leetcode.com/problems/course-schedule-iii/

import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        current = 0
        heap = []

        for course in courses:
            if current + course[0] <= course[1]:
                current += course[0]
                heapq.heappush(heap, -course[0])
            elif len(heap) != 0 and current + course[0] > course[1] and course[0] < -heap[0]:
                current += heapq.heappop(heap) + course[0]
                heapq.heappush(heap, -course[0])

        return len(heap)
